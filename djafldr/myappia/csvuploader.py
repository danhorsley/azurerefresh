from .models import BookData
import csv
path = 'somepath'
 
with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = BookData.objects.get_or_create(
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

