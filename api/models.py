from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import DateField
# Create your models here.

class Answer(models.Model):
    user_answer=models.CharField(max_length=200)

    class Meta:
        #abstract=True
        ordering=['id']

    def __str__(self):
        return self.user_answer

class Quizzes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    original_answer=models.CharField(max_length=100)
    option_one=models.CharField(max_length=100)
    option_two=models.CharField(max_length=100,default='NA')
    option_three=models.CharField(max_length=100,default='NA')
    option_four=models.CharField(max_length=100,default='NA')
    publish_date=DateField()

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.question