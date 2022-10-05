import requests
import csv
import json 
import datetime

def covertTodate(date):
    format = '%Y/%m/%d'
    covDate = datetime.datetime.strptime(date, format)
    return covDate

url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
res = requests.get(url)
response = json.loads(res.text)

with open('data.csv',mode='w',newline='') as data_file:
    writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for item in response['result']['results']:
        date = item['xpostDate']
        year = covertTodate(date).year
        if (year >= 2015):
            address = item['address']
            index = address.rfind(" ")+1
            district = address[index:index+3]
            title = item['stitle']
            longitude = item['longitude']
            latitude = item['latitude']
            pic = item['file'].split("https://")
            writer.writerow([title,district, longitude,latitude,"https://" + pic[1]])


