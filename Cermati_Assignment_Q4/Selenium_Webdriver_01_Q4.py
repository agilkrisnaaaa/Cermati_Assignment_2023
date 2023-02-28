# Manually written script for Selenium WebDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome();

driver.get('http://cermati.com/app/gabung');

driver.find_element(By.ID, 'email').send_keys('agilkrisna01@gmail.com')
driver.find_element(By.ID, 'mobilePhone').send_keys('085156350536')
driver.find_element(By.ID, 'password').send_keys('Password123!')
driver.find_element(By.ID, 'confirmPassword').send_keys('Password123!')
driver.find_element(By.ID, 'firstName').send_keys('Agil')
driver.find_element(By.ID, 'lastName').send_keys('Krisna Tripujianto')
driver.find_element(By.ID, 'cityAndProvince').send_keys('KOTA TANGERANG')
driver.find_element(By.ID, 'terms-and-condition').click()
driver.find_element(By.CSS_SELECTOR, ".RegistrationForm_form-container__button-text__k6N8W").click()

pdb.set_trace()