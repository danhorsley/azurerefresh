from myappia.models import BookData, DailyData
import os
import csv
from datetime import datetime


def dateconverter(my_date):
        return datetime.strptime('2020-11-12 11:21:59+00:00', '%Y-%m-%d %H:%M:%S+00:00')
def blanker(my_input):
        if my_input == '':
            return 0
        else:
            return my_input

def bookuploader(reset = False): 
    if reset:
        BookData.objects.all().delete()  
    counter = 1
    with open("bookuploaddata1.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                counter+=1
                print(counter)
                bd = BookData(
                    isbn10=row[0],
                    isbn13=row[1],
                    title=row[2],
                    asr=row[3],
                    stock=row[4],
                    offers=row[5],
                    cost=row[6],
                    salepx=row[7],
                    sales90d=row[8],
                    cover=row[9]
                )
                bd.save()

def dailydatauploader(reset = False): 
    if reset:
        DailyData.objects.all().delete()  
    counter = -1
    with open("daily_data.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                counter+=1
                if counter == 0:
                    pass
                else:
                    print(counter)
                    dd = DailyData(
                        date=datetime.strftime(dateconverter(row[0]), '%Y-%m-%d %H:%M:%S'),
                        isbn10=row[1],
                        itemname=row[2][:50],
                        quantity=row[3],
                        fulfilment=row[4],
                        productsales=row[5],
                        postagecredits=row[6],
                        sellingfees=row[7],
                        fbspfees=row[8],
                        total=row[9],
                        isbn13=row[10],
                        cost=blanker(row[11]),
                        net_profit=blanker(row[12]),
                    )
                    dd.save()

