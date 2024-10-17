from django.db import models
from django.contrib.auth.models import User
import random

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500) 
    span = models.TextField(blank=True, null=True)   
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Продолжительность квиза", default="1")
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    
class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Вопрос: {self.question.content}, Ответ: {self.content}, Правильный ответ: {self.correct}"
    
class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.quiz)


