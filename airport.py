import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


"""
with open ('D:\Internship/airportcode.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        print(line[0])
"""

PATH=  "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.wikipedia.org/")

search=driver.find_element_by_name("search")
search.send_keys("TLH Airport")
search.send_keys(Keys.RETURN)

url = driver.current_url
response= requests.get(url)
soup= BeautifulSoup(response.text, 'lxml')


iata_info= soup.find('span', class_='nickname').text
icao_info= soup.find('span', class_='nowrap').a.text
location_info= soup.find('td', class_='label').text

print(iata_info)
print(icao_info)
print(location_info)



'''
url='https://en.wikipedia.org/wiki/Tribhuvan_International_Airport'
class_name= 'nickname'

response= requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')


info= soup.find('span', attrs={'class':class_name})
print (info)
'''