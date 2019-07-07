# mongodb://dil23:chess004@ds159866.mlab.com:59866/munwaththa
from pymongo import *
import pandas as pd

MONGODB_URI = ""
client = MongoClient(MONGODB_URI, connectTimeoutMS=1900000)
db = client.get_database("ukuthule")
mathes = db.vibagas



#insert a record
db.vibagas.insert_one({
"year": "2020",
"studentId": "2091",
 "grade5": "128"

})




print(db.mathes.distinct("stu")) #get the distinct values

students =  db.mathes.find_one()
print(students)

# Get lists of the fields present in each type of document
students_fields = list(students.keys())
print(students_fields)


#get the count mathches the filter
count = db.mathes.count_documents({
   
   'stu':'1789'

	})

print(count)

#saving to a csv

data = pd.DataFrame(list(mathes.find()))


data.to_csv('ukuthule_exams.csv')



####push csv to db
import csv
import json
import pandas as pd
import sys, getopt, pprint
#CSV to JSON Conversion
csvfile = open('test.csv', 'r')
reader = csv.DictReader( csvfile )
 
db.segment.drop()
header= [ "S_No", "Instrument_Name"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)


######