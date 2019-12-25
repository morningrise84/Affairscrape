# LOAD MODULES #
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# PREPARE .CSV TO STORE PROFILE LINKS #
exportcsv = open('Profiles.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['ID', 'Nickname', 'Age', 'Location', 'Status', 'Match', 'Height', 'Weight', 'Figure', 'Smoker', 'Desired Height', 'Desired Age', 'Profile Link'])

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
        try:
            popup = WebDriverWait(driver, 10).until(ec.element_to_be_clickable([By.XPATH, '//*[@id="overlayerClose"]']))
            popup.click()
        except Exception as e:
            pass
        time.sleep(3)

# PARSE DATA #
        link = driver.current_url
        ID = link.split('/')[5]
        ID = ID.split('?')[0]
        nickname = driver.find_element_by_xpath("/html/body/app-root/loggedin/div[2]/user-profile/div/div[1]/div/div[2]/div/m-action-photo/div/div[2]/div[3]/p[1]/strong").text
        location = driver.find_element_by_xpath("/html/body/app-root/loggedin/div[2]/user-profile/div/div[1]/div/div[2]/div/m-action-photo/div/div[2]/div[3]/span").text
        extras = driver.find_element_by_xpath("/html/body/app-root/loggedin/div[2]/user-profile/div/div[1]/div/div[2]/div/m-action-photo/div/div[2]/div[3]/p[2]").text
        age = extras.split(' |')[0]
        age = extras.split(' Jahre')[0]
        height = extras.split('| ')[1]
        height = height.replace(' cm', '')
        status = extras.split('| ')[2]
        match = driver.find_element_by_xpath("/html/body/app-root/loggedin/div[2]/user-profile/div/div[2]/div[1]/div/strong").text
        match = match.split('%')[0]

        try:
            weightQ = driver.find_element_by_xpath("//*[contains(text(), 'Körpergewicht')]")
            weightA = weightQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            weightA = weightA.split('class="item">')[1]
            weightA = weightA.split(' kg')[0]
        except Exception as e:
            weightA = 'N/A'

        try:
            figureQ = driver.find_element_by_xpath("//*[contains(text(), 'Figur')]")
            figureA = figureQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            figureA = figureA.split('class="item">')[1]
            figureA = figureA.split('</span>')[0]
        except Exception as e:
            figureA = 'N/A'

        try:
            smokerQ = driver.find_element_by_xpath("//*[contains(text(), 'Rauchverhalten')]")
            smokerA = smokerQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            smokerA = smokerA.split('class="item">')[1]
            smokerA = smokerA.split('</span>')[0]
        except Exception as e:
            smokerA = 'N/A'

        try:
            desiredheight = driver.find_element_by_xpath('//*[@id="searching-for"]/div/div/a-expandable-area/div/a-definition-list/div/div[3]/div[2]/div/span').get_attribute('innerHTML')
        except Exception as e:
            desiredheight = 'N/A'

        try:
            desiredage = driver.find_element_by_xpath('//*[@id="searching-for"]/div/div/a-expandable-area/div/a-definition-list/div/div[2]/div[2]/div/span').get_attribute('innerHTML')
        except Exception as e:
            desiredage = 'N/A'

        print(ID)
        print(nickname)
        print(age)
        print(location)
        print(status)
        print(match)
        print(height)
        print(weightA)
        print(figureA)
        print(smokerA)
        print(desiredheight)
        print(desiredage)
        print(link)

# EXPORT PROFILES TO .CSV #
        csvwriter.writerow([ID, nickname, age, location, status, match, height, weightA, figureA, smokerA, desiredheight, desiredage, link])

if __name__ == '__main__':
    with open ('Links.csv') as url_obj:
        csv_url_reader(url_obj)

exportcsv.close()

driver.close()
