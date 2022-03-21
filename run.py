import os
from os.path import join, dirname
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

salarium_creds = {'email': os.environ.get("email"),
                  'password': os.environ.get("password")
                  }
#Headless Browser                  
op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe',options=op)
driver.get('https://app.salarium.com/users/login')
time.sleep(5)

email_textbox = driver.find_element_by_name("email")
email_textbox.send_keys(salarium_creds['email'])
time.sleep(2)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(salarium_creds['password'])
time.sleep(2)

login_button = driver.find_element_by_class_name("btn-form-custom")
login_button.submit()
time.sleep(5)

# clock_button = driver.find_element_by_xpath("//div[@class='button-group']//button[@id='time_btn']")
# clock_button.click()

clock_button = driver.find_element_by_xpath("/html/body/div[2]/section/section/section/div[2]/div[1]/section[1]/div/div/div[2]/button")
driver.execute_script("arguments[0].click();", clock_button)
print("Clocked Successfully")
time.sleep(2)
driver.quit()

# adding this for git testing purposes