import os
import time

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import threading

driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
driver = uc.Chrome(version_main=int(driver_version))
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 20)

language_menu = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language_menu.click()

cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

# TESTING AREA

buildings = driver.find_elements(By.CSS_SELECTOR, "#store div")
building_ids = [building.get_attribute("id") for building in buildings[:-1]]

# DEF GET ALL AVAILABLE PRODUCTS 
for building in buildings:
    if building.get_attribute("class") == "product locked disabled":
        print(building.get_attribute("id"))

while True:
    try:
        cookie.click()  
        time.sleep(0.1) 
    except: 
        print("Couldn't click the cookie.")

time.sleep(10)

driver.quit()