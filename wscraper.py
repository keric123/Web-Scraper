import pandas as pd
import test
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path =("C:/Users/Win10/Desktop/scraper/chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:/Users/Win10/Desktop/scraper/chromedriver.exe")

driver.get("C:/Users/Win10/Desktop/scraper/test.html")
results = []
content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

for element in soup.findAll(attrs="label"):
    name = element.find("span")

df = pd.DataFrame({"Rezultati": results})
df.to_csv("rezultati.csv", index=False, encoding="utf-8")


