from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

service = Service(
    executable_path="C:/chromedriver_win32/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store data
course_codes = []  
titles = []
descriptions = []
clo1_list = []
clo2_list = []
clo3_list = []
clo4_list = []
textbook1_list = []
textbook2_list = []
instructors = []
semesters = []

driver.get("http://eduko.spikotech.com/Course/Index")
sleep.sleep(2) 

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# Loop through each course card
for card in soup.findAll("div", attrs={"class": "card"}):
    course_code = card.find('a')['href'].split('/')[-1]  # Extract Course Code from URL
    title = card.find('h4', class_='card-title').text.strip() if card.find('h4', class_='card-title') else ""
    description = card.find('p', class_='card-text').text.strip() if card.find('p', class_='card-text') else ""
    # details_url = "http://eduko.spikotech.com/Course" + card.find('a')['href']
    # driver.get(details_url)
    # sleep.sleep(2) 

    # detail_content = driver.page_source
    # detail_soup = BeautifulSoup(detail_content, features="html.parser")
    # clo1 = detail_soup.find('div', id='clo1').text.strip() if detail_soup.find('div', id='clo1') else ""
    # clo2 = detail_soup.find('div', id='clo2').text.strip() if detail_soup.find('div', id='clo2') else ""
    # clo3 = detail_soup.find('div', id='clo3').text.strip() if detail_soup.find('div', id='clo3') else ""
    # clo4 = detail_soup.find('div', id='clo4').text.strip() if detail_soup.find('div', id='clo4') else ""
    # textbook1 = detail_soup.find('div', id='textBook1').text.strip() if detail_soup.find('div', id='textBook1') else ""
    # textbook2 = detail_soup.find('div', id='textBook2').text.strip() if detail_soup.find('div', id='textBook2') else ""
    
    instructor = card.find('h7').text.strip() if card.find('h7') else ""
    semester = card.find_all('h7')[1].text.strip() if len(card.find_all('h7')) > 1 else ""

    # Append the extracted data to the lists
    course_codes.append(course_code)
    titles.append(title)
    descriptions.append(description)
    # clo1_list.append(clo1)
    # clo2_list.append(clo2)
    # clo3_list.append(clo3)
    # clo4_list.append(clo4)
    # textbook1_list.append(textbook1)
    # textbook2_list.append(textbook2)
    instructors.append(instructor)
    semesters.append(semester)

# Create a DataFrame with the collected data
df = pd.DataFrame({
    "CourseCode": course_codes,
    "Title": titles,
    "Description": descriptions,
    # "CLO1": clo1_list,
    # "CLO2": clo2_list,
    # "CLO3": clo3_list,
    # "CLO4": clo4_list,
    # "TextBook1": textbook1_list,
    # "TextBook2": textbook2_list,
    "Instructor": instructors,
    "Semester": semesters
})

df.to_csv("eduiko_courses.csv", index=False, encoding="utf-8")

driver.quit()  # Close the browser
