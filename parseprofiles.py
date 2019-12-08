# LOAD MODULES #
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# PREPARE .CSV TO STORE PROFILE LINKS #
exportcsv = open('Profiles.csv', 'w', newline='')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['Nickname', 'Age', 'Height', 'Status', 'Match'])

# CREDENTIALS #
username = '' # Insert your credentials here
password = '' # Insert your credentials here

# CHROME PREPARATION AND TARGET DEFINITION #
chrome = r"""C:\Users\HP\Desktop\chromedriver.exe""" # ChromeDriver is needed, select here the folder where it is stored
driver = webdriver.Chrome(chrome)
driver.get('https://www.secret.de/login')
time.sleep(2)
driver.maximize_window()
time.sleep(2)

# HANDLE COOKIES #
cookie = WebDriverWait(driver, 5, 0.25).until(ec.visibility_of_element_located([By.XPATH, '/html/body/div[1]/div[1]/div/button']))
cookie.click()
time.sleep(2)

# LOGIN #
login = driver.find_element_by_xpath('//*[@id="login_username"]')
login.send_keys(username)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="login_password"]')
login.send_keys(password)
time.sleep(2)
login.send_keys(Keys.RETURN)
time.sleep(2)

def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj, delimiter = ',')
    for line in reader:
        url = line['Link']
        driver.get(url)
        popup = WebDriverWait(driver, 10).until(ec.element_to_be_clickable([By.XPATH, '//*[@id="overlayerClose"]']))
        popup.click()
        time.sleep(2)

# PARSE DATA #
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find('div', class_ ='my-profile my-profile__has-navigation')
        nickname = results.find('p', attrs={'class' : 'text-nickname mb-1'}).text
        extras = results.find('p', attrs={'class' : 'ng-star-inserted'}).text
        age = extras.split(' |')[0]
        age = extras.split(' Jahre')[0]
        height = extras.split('| ')[1]
        height = height.replace(' cm', '')
        status = extras.split('| ')[2]
        match = results.find('div', {"class": 'my-profile__matching-text container__padding text-virgo'}).text
        match = match.split(':')[1]
        match = match.split('%')[0]
        print(nickname)
        print(age)
        print(height)
        print(status)
        print(match)

        print()

# EXPORT PROFILES TO .CSV #
        csvwriter.writerow([nickname, age, height, status, match])

if __name__ == '__main__':
    with open ('Links.csv') as url_obj:
        csv_url_reader(url_obj)

exportcsv.close()

driver.close()
