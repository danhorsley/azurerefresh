from myappia.models import BookData
import os
import csv

def bookuploader(): 
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
                    sales90d=row[8]
                )
                bd.save()

