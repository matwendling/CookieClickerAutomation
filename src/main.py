import os
import time

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
driver = uc.Chrome(version_main=int(driver_version))
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 20)

language_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")))
language_menu.click()

cookie = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[15]/div[8]/button")))
cookie.click()

time.sleep(10)

driver.quit()