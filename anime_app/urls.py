from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

urlpatterns = [
    path('quizzes/', views.QuizView.as_view()),
    path('quizzes/<int:quiz_id>/', views.QuizDetail.as_view(), name='quiz-detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('quiz/<int:quiz_id>/result/', views.UserResult.as_view(), name='result')
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]