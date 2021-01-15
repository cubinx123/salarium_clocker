import os
from os.path import join, dirname
from dotenv import load_dotenv
import time
from selenium import webdriver

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

salarium_creds = {'email': os.environ.get("email"),
                  'password': os.environ.get("password")
                  }

driver_details = {
                  'driver': os.environ.get("driver_name"),
                  'driver_path': os.path.dirname(os.path.abspath(__file__)) + '\\'
                  }

# print(driver_details['driver_path'] + driver_details['driver'])


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://app.salarium.com/users/login')
time.sleep(3)

email_textbox = driver.find_element_by_name("email")
email_textbox.send_keys(salarium_creds['email'])
time.sleep(5)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(salarium_creds['password'])
time.sleep(5)

login_button = driver.find_element_by_class_name("btn-form-custom")
login_button.submit()
time.sleep(15)

clock_button = driver.find_element_by_id("time_btn")
clock_button.click()