from django.db import models

class Genres(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.username


class UserDetail(models.Model):
    name = models.TextField()
    surname = models.TextField()
    email = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='detail')


class Questions(models.Model):
    SINGLE = 'single'
    MULTIPLE = 'multiple'
    TRUEFALSE = 'true_false'
    TYPE_CHOICES = [
        (SINGLE, 'Single choice'),
        (MULTIPLE, 'Multiple choice'),
        (TRUEFALSE, 'True/False'),
    ]

    text = models.TextField()
    image_url = models.CharField(max_length=255)  # путь к изображению
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='questions')
    genres = models.ManyToManyField(Genres, related_name='questions')



class Option(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options')
    text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text


class Quizzes(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)  # путь к изображению
    # image = models.ImageField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='quizzes')
    difficulty = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genres, related_name='quizzes')
    questions = models.ManyToManyField(Questions, related_name='quizzes')

    def __str__(self):
        return self.title

class UserResult(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE, related_name='results')
    started_at = models.TimeField()
    finished_at = models.TimeField()
    score = models.BigIntegerField()
    total = models.BigIntegerField()

    def __str__(self):
        return f"{self.user} - {self.quiz} {self.score}/{self.total}"