from django.db import models
from django.utils import timezone
import datetime

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

class SalesData(models.Model):
    xsin = models.CharField(max_length=20) #will link to isbn10 later
    date = models.DateTimeField()
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=1)
    salesfees = models.FloatField(default=0)
    postage = models.FloatField(default=0)

class BookStatic(models.Model):
    isbn = models.CharField(max_length=10)
    title1 = models.CharField(max_length=200)
    datefirstbot = models.DateTimeField()

class InvoiceData(models.Model):
    isbn13 = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    cost = models.FloatField(default=1)
    totalprice = models.FloatField(default=1)
    date = models.DateTimeField()
    wholesaler = models.CharField(max_length=1)

class DailyData(models.Model):
    date = models.DateTimeField()
    isbn10 = models.CharField(max_length=20)
    itemname = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    fulfilment = models.CharField(max_length=20)
    productsales = models.FloatField(default=0)
    postagecredits = models.FloatField(default=0)
    sellingfees = models.FloatField(default=0)
    fbspfees = models.FloatField(default=0)
    total = models.FloatField(default=0)
    isbn13 = models.CharField(max_length=20)
    cost = models.FloatField(default=0)
    net_profit = models.FloatField(default=0)

