import urllib.request, urllib.parse, urllib.error 
import csv
from bs4 import BeautifulSoup
import requests
import time

#csv file to export data
csv_infofile=open('D:\Internship/airport/airport_info.csv', 'w')
csv_writer= csv.writer(csv_infofile)
csv_writer.writerow(['iata','icao','airport_name','location','gps'])


def site(code): #takes iata code as parameter
    '''
    url='https://en.wikipedia.org/wiki/'
    value= code+'_Airport'
    url2=url+value
    data=value.encode('utf-8')
    req= urllib.request.Request(url,data)
    resp= urllib.request.urlopen(req)
    resp_data=requests.get(url2)
    '''
    url='https://en.wikipedia.org/wiki/'+code+'_Airport'
    resp_data=requests.get(url)
    return resp_data #return html text file

#importing csv file
csv_file =open ('D:\Internship/airport/airportcode.csv', 'r') 
csv_reader= csv.reader(csv_file)
next(csv_reader) #skipping first line
    
# the loop   
for line in csv_reader:
    code=line[0] #iata code
    print (code)
    response= site(code)
    soup= BeautifulSoup(response.text, 'lxml')
  

    #get iata and icao codes
    try:
        info1= soup.find_all('span', class_='nickname')
        iata_info=code
        icao_info=info1[1].text
    except:
        icao_info='unknown'


    #get airport name
    try:
        name= soup.find('div', class_='fn org').text
    except:
        name='unknown'
        

    #get location
    info2=soup.find_all('tr')
    info3=soup.find_all('td', class_='label')
    try:
        location=info3[0].text
    except:
        location='unknown'
    #location=info2[6].td.a.text.split(',')
    #city=location[0].strip()
    #country=location[1].strip()

    #get gps
    try:
        gps=soup.find('span', class_="geo-dec").text
    except:
        gps='unknown'

    #get elevation
    #elevation_info=info2[8].td.text
    #elevation_info=soup.find_all('th', {'scope':'row'})[4].next_sibling.text

    #export data in the csv file
    try:
        csv_writer.writerow([iata_info, icao_info,name, location, gps])
    except:
        csv_writer.writerow([iata_info,'unknown','unknown','unknown','unknown' ])

    time.sleep(1)