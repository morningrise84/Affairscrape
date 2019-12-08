# LOAD MODULES #
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# PREPARE .CSV TO STORE PROFILE LINKS #
exportcsv = open('Links.csv', 'w', newline='')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['Link'])

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

# CLOSE POPUS & RETRIEVE PROFILE LINKS #
for i in range(3):
    pages = driver.get('https://www.secret.de/my/search?index={}'.format(i+1))
    popup = WebDriverWait(driver, 10).until(ec.element_to_be_clickable([By.XPATH, '//*[@id="overlayerClose"]']))
    popup.click()
    time.sleep(2)
    links = driver.find_elements_by_xpath("//a[contains(@href, '/my/profile/')]")
    for ii in links:
        print(ii.get_attribute('href'))

# EXPORT PROFILE LINKS TO .CSV #
        csvwriter.writerow([ii.get_attribute('href')])

exportcsv.close()

driver.close()