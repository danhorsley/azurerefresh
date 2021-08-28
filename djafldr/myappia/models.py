from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class BookData(models.Model):
    isbn10 = models.CharField(max_length=20)
    isbn13 = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    asr = models.IntegerField(default=2000000)
    stock = models.IntegerField(default=1500)
    offers = models.IntegerField(default=20)
    cost = models.FloatField(default = 1.5)
    salepx = models.FloatField(default = 4.0)
    sales90d = models.IntegerField(default = 0)
    cover = models.CharField(default="Paperback",max_length=20)
