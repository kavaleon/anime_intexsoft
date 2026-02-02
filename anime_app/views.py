from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import tokens
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.hashers import make_password

from .serializers import LoginSerializer, QuizSerializer
from .models import Quizzes, Questions, Users



class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')
        is_admin = False

        if not username or not password:
            return Response({'error: Введите имя пользователя или пароль'})
        if not Users.objects.filter(username=username).exists:
            return Response({'error: Пользователь с таким именем пользователя уже существует'})
        
        hashed_password = make_password(password)
        print('im here')
        Users.objects.create(username=username, password_hash=hashed_password, is_admin= is_admin)
        print('right')
        return Response({'message: Регистрация прошла успешно'}, status=status.HTTP_200_OK)



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            print(str(refresh), str(refresh.access_token))
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    def post(self, request):
        
        return Response({"message": "Вы успешно вышли"})
    


class QuizView(APIView):
    def get(self, request):
        quizzes = Quizzes.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
