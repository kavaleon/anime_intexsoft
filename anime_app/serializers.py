from rest_framework import serializers
from .models import Quizzes, Questions, Users
from django.contrib.auth import authenticate

from django.contrib.auth.hashers import check_password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise serializers.ValidationError("Некорректные логин или пароль")
        
        
        if not check_password(password, user.password_hash):
            raise serializers.ValidationError("Некорректные логин или пароль")
        """{"username":"ulyana","password":"8784858689u"}"""
        
        return user
    

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = '__all__' 

