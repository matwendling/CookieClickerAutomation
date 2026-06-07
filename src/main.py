import os
import time
import threading

import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
driver = uc.Chrome(version_main=int(driver_version))
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 20)

language_menu = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language_menu.click()

cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

# TESTING AREA

buildings = driver.find_elements(By.CSS_SELECTOR, "#products div")
fetch_all_available_buildings

while True:
    try:
        cookie.click()  
        time.sleep(0.1) 
    except: 
        print("Couldn't click the cookie.")

time.sleep(10)

driver.quit()