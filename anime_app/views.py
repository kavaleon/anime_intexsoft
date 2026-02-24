from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django_redis import get_redis_connection
from django.contrib.auth.hashers import make_password
from datetime import datetime, time, timedelta
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, UserResultSerializer
from .models import Quizzes, Questions, Users, UserResult

from rest_framework_simplejwt.tokens import AccessToken, TokenError


def get_user_from_access_token_or_refresh(request):
    access_token = request.COOKIES.get('access_token')
    refresh_token = request.COOKIES.get('refresh_token')

    if not access_token:
        if not refresh_token:
            return None, Response({'detail': 'Токен отсутствует, авторизация необходима'}, status=401)

        redis_conn = get_redis_connection("default")
        redis_key = f"refresh_token:{refresh_token}"

        if not redis_conn.get(redis_key):
            return None, Response({'detail': 'Недопустимый рефреш-токен'}, status=401)

        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)

            response = Response()
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                httponly=True,
                secure=False,
                max_age=300,
                samesite='Lax',
                path='/'
            )

            return {'response': response}, None
        except TokenError:
            redis_conn.delete(redis_key)
            return None, Response({'detail': 'Рефреш-токен недействителен'}, status=401)


    try:
        token = AccessToken(access_token)
        user_id = token.get('user_id')
        if not user_id:
            return None, Response({'detail': 'Некорректный токен'}, status=401)

        user = Users.objects.filter(id=user_id).first()
        if not user:
            return None, Response({'detail': 'Пользователь не найден'}, status=401)

        return user, None

    except TokenError:
        if not refresh_token:
            return None, Response({'detail': 'Токен недоступен'}, status=401)
        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            response = Response()
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                httponly=True,
                secure=False,
                max_age=300,
                samesite='Lax',
                path='/'
            )
            return get_user_from_access_token_or_refresh(request._request), response
        except TokenError:
            redis_conn = get_redis_connection("default")
            redis_conn.delete(f"refresh_token:{refresh_token}")
            return None, Response({'detail': 'Рефреш-токен недействителен'}, status=401)
        


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')
        is_admin = False


        if not username or not password:
            return Response({'error: Введите имя пользователя или пароль'}, status=status.HTTP_400_BAD_REQUEST)
        

        if not Users.objects.filter(username=username).exists:
            return Response({'error: Пользователь с таким именем пользователя уже существует'})
    

        Users.objects.create(username=username, password_hash=make_password(password), is_admin= is_admin)
        return Response({'message': 'Регистрация прошла успешно'}, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return Response({'message': 'Неверное имя пользователя или пароль'}, status=status.HTTP_401_UNAUTHORIZED)

        if not check_password(password, user.password_hash):
            return Response({'message': 'Неверное имя пользователя или пароль'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken()
        refresh['user_id'] = user.id
        refresh['username'] = user.username
        refresh.set_exp(lifetime=timedelta(days=30))

        access = refresh.access_token
        access.set_exp(lifetime=timedelta(days=1))


        redis_conn = get_redis_connection("default")
        redis_key = f"refresh_token:{str(refresh)}"
        cookie_max_age = 30 * 24 * 60 * 60
        redis_conn.set(redis_key, user.id, ex=cookie_max_age)


        response = Response({'username': user.username}, status=status.HTTP_200_OK)
        

        response.set_cookie(
            key='access_token',
            value=str(access),
            httponly=True,
            secure=False,
            max_age=24*60*60,
            samesite='Lax',
            path='/',
        )

        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=False,
            max_age=cookie_max_age,
            samesite='Lax',
            path='/',
        )

        return response
    

class LogoutView(APIView):
    def post(self, request):
        redis_conn = get_redis_connection("default")
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token:
            redis_key = f"refresh_token:{refresh_token}"
            redis_conn.delete(redis_key)

        response = Response({'message': 'Выход выполнен'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token', path='/')
        response.delete_cookie('refresh_token', path='/')
        return response


class QuizView(APIView):
    def get(self, request):
        quizzes = Quizzes.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class QuizDetail(APIView):
    def get(self, request, quiz_id):
        try:
            quiz = Quizzes.objects.get(id=quiz_id)
            questions = quiz.questions.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        except Quizzes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserQuizResultView(APIView): 
    def post(self, request, quiz_id): 
        answers = request.data.get('answers') 
        total, score = 0, 0

        for answer in answers:
            if answer:
                total += 1
                if answer['is_correct']:
                    score += 1

        result = {
            "total": total,
            "score": score,
            "quiz_id": quiz_id,
        }
        print(datetime.now())
        user, resp = get_user_from_access_token_or_refresh(request)
        print(user, resp)
        if user:
            print('im here')
            UserResult.objects.create(
                started_at=datetime.now(),
                finished_at=datetime.now(),
                score=score,
                total=total,
                quiz_id=quiz_id,
                user_id=user.id,
        )

        return Response(result, status=status.HTTP_200_OK)


class UserAuthCheckView(APIView):
    def get(self, request):
        user, resp = get_user_from_access_token_or_refresh(request)
        if not user:
            return resp  

        serializer = UserSerializer(user)
        return Response(serializer.data)
        

class UserResultsView(APIView):
    def get(self, request, user_id):
        
        user, resp = get_user_from_access_token_or_refresh(request)
        if not user:
            return resp

        results = UserResult.objects.filter(user=user).select_related('quiz')
        serializer = UserResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
