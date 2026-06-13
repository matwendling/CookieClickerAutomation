import os
import time
import threading
from typing import Any

import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from app.buildings.domain.dtos.building_dto import BuildingDTO
from app.upgrades.domain.dtos.upgrade_dto import UpgradeDTO

driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
driver = uc.Chrome(version_main=int(driver_version))
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 20)

language_menu = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language_menu.click()

# TESTING AREA

### COOKIE FUNCTIONS

def click_on_cookie():
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()
    time.sleep(0.1)

### BUILDINGS AND UPGRADES

def get_all_available_buildings(self, driver: uc.Chrome) -> list[BuildingDTO]:
        all_buildings = []
        buildings = driver.find_elements(By.CSS_SELECTOR, "#products div")
        for building in buildings:
            if building.get_attribute("class") == "product locked disabled":
                building_id = building.get_attribute("id")
                building_name = driver.find_element(By.ID, f"productName{building_id[-1]}").text
                building_price = driver.find_element(By.ID, f"productPrice{building_id[-1]}").text
                building_cps = 5 # figure out later

                all_buildings.append(
                    BuildingDTO(
                        id=building_id,
                        name=building_name,
                        price=building_price,
                        cookies_per_second=building_cps
                    )
                )
        
        return all_buildings

def get_all_available_upgrades(self, driver: uc.Chrome) -> list[UpgradeDTO]:
    all_upgrades = []
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div")
    for upgrade in upgrades:
        upgrade_id = upgrade.get_attribute("id")
        upgrade_name = upgrade.get_attribute("")
        upgrade_cost = upgrade.get_attribute()
        upgrade_effect = upgrade.get_attribute()

########

def get_best_available_building_info(buildings: list[dict[Any]]) -> BuildingDTO:
    best_building = {"id": "", "name": "", "price": 0, "cps": 0}
    for building in buildings:
        if building["cps"] > best_building["cps"]:
            best_building["id"],
            best_building["name"], 
            best_building["price"],
            best_building["cps"] = building["id"], building["name"], building["price"], building["cps"]

    return BuildingDTO(
        best_building["id"],
        best_building["name"],
        best_building["price"],
        best_building["cps"]
    )

def get_best_available_upgrade_info(upgrades: list[dict[Any]]) -> UpgradeDTO:
    best_upgrade = {"id": "", "name": "", "price": 0, "cps": 0}
    for upgrade in upgrades:
        pass
        
######## MAIN PROGRAM 

time.sleep(3)

count = 0
cookie_thread = threading.Thread(target=click_on_cookie)

while count <= 100000:
    try:
        cookie_thread.start()
        count += 1
    except:
        print()