from django.contrib import admin
from .models import Users, Quizzes, Questions, Genres, UserDetail, Option


admin.site.register(Users)
admin.site.register(Quizzes)
admin.site.register(Questions)
admin.site.register(Option)
admin.site.register(Genres)
admin.site.register(UserDetail)