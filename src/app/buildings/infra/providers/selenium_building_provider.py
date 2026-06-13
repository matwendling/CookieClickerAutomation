from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from app.buildings.domain.dtos.building_dto import BuildingDTO
from app.buildings.domain.providers.i_building_provider import IBuildingProvider
import undetected_chromedriver as uc
import os

class ChromeBuildingProvider(IBuildingProvider):
    def __init__(self):
        driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
        driver = uc.Chrome(version_main=int(driver_version))
        driver.get("")

        self.driver = driver

    def get_building_element(self, driver: Chrome) -> BuildingDTO:
        """
        Fetches one Building from the DOM.
        """
    
    def get_all_available_buildings(self, driver: Chrome) -> list[BuildingDTO]:
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
    
    # TESTS!

    def get_all_available_buildings_filterless(self) -> list[str]:
        return self.driver.find_elements(By.CSS_SELECTOR, "#products div")

    def get_all_available_buildings(self) -> list[str]:
        buildings = self.driver.find_elements(By.CSS_SELECTOR, "#products div")
        return [building.get_attribute("id") for building in buildings if building.get_attribute("class") == "product unlocked enabled"]
    
    def get_building_data(self, building_id: str) -> BuildingDTO:
        building_name = self.driver.find_element(By.ID, f"productName{building_id[-1]}").text
        building_price = self.driver.find_element(By.ID, f"productPrice{building_id[-1]}").text
        building_cps = 5 # figure out later

        return BuildingDTO(building_id, building_name, building_price, building_cps)
        
    def __cookies_per_second_tooltip_handler(): 
        pass