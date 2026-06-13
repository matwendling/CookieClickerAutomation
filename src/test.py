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

price_test = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]/div[3]/span[2]")))
price_test.text
print(price_test.text) # "15"
print(type(price_test.text)) # str

time.sleep(10)

driver.quit()

# TEST

def get_all_available_upgrades_id() -> list[str]:
    all_upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div")
    return [upgrade.get_attribute("id") for upgrade in all_upgrades]

def get_all_available_buildings_id() -> list[str]:
    all_buildings = driver.find_elements(By.CSS_SELECTOR, "#products div")
    return [building.get_attribute("id") for building in all_buildings if building.get_attribute("class") == "product unlocked enabled"]