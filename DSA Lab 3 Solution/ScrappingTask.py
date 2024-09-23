from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

# webdriver can be downloaded from
# https://sites.google.com/chromium.org/driver/downloads/versionselection?authuser=0

service = Service(
    executable_path="C:\Program Files\chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')

products = []  # List to store name of the product
prices = []  # List to store price of the product
original_prices=[]
# ratings = []  # List to store rating of the product

driver.get("https://www.aliexpress.com/w/wholesale-racing-cars.html?spm=a2g0o.home.search.0")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("div", attrs={"class":"list--galleryWrapper--29HRJT4"}):
    print(a)
    name = a.find("div", attrs={"class": "sale-title"})
    price = a.find("div", attrs={"class": "sale-price"})
    original_price=a.find("div", attrs={"class": "origin-price"})
    if name != None and price != None:
        products.append(name.txt)
        prices.append(price.text)
        original_prices.append(original_price)
    if len(products) == 50:
        break

df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("Daraz.csv", index=False, encoding="utf-8")