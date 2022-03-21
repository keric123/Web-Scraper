import pandas as pd
import test
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#here you import all of the required libraries

chrome_driver_path =("C:/Users/Win10/Desktop/scraper/chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:/Users/Win10/Desktop/scraper/chromedriver.exe")
#this part was about using a chrome driver if you are using a Chrome browser; there is also this for Mozilla.

driver.get("C:/Users/Win10/Desktop/scraper/test.html")
results = []
content = driver.page_source
soup = BeautifulSoup(content, features="lxml")
#What this does is tells the driver from where it scrapes.

for element in soup.findAll(attrs="label"):
    name = element.find("span")
#This is an important part as you need to know some HTML and to navigate via inspect function in browser to find what you want to scrape.
    
    
df = pd.DataFrame({"Rezultati": results})
df.to_csv("rezultati.csv", index=False, encoding="utf-8")
# this final part of code is configuring and using pandas to convert and store data in .csv format.

