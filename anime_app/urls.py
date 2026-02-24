from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

urlpatterns = [
    path('quizzes/', views.QuizView.as_view()),
    path('quizzes/<int:quiz_id>/', views.QuizDetail.as_view(), name='quiz-detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),
    path('quiz/<int:quiz_id>/result/', views.UserQuizResultView.as_view(), name='result'),
    path('user/', views.UserAuthCheckView.as_view(), name='user'),
    path('user/<int:user_id>/results', views.UserResultsView.as_view(), name='user_results')
]