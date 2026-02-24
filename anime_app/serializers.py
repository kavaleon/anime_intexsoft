from rest_framework import serializers
from .models import Quizzes, Questions, Users, Option, UserResult


class OptionSerializer(serializers.ModelSerializer):
    '''сериализатор для модели Options'''
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    '''сериализатор для модели Questions'''
    options = OptionSerializer(many=True)
    class Meta:
        model = Questions
        fields = ['id', 'text', 'image_url', 'type', 'options']


class QuizSerializer(serializers.ModelSerializer):
    '''сериализатор для модели Quizes'''
    class Meta:
        model = Quizzes
        fields = '__all__' 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'is_admin']


class UserResultSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    quiz = QuizSerializer()

    class Meta:
        model = UserResult
        fields = ['id', 'user', 'quiz', 'started_at', 'finished_at', 'score', 'total']