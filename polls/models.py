from datetime import timezone, datetime
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Answer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice,on_delete=models.DO_NOTHING)
