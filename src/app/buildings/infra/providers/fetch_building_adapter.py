from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By

from cookie_clicker.src.app.buildings.domain.dtos.building_dto import BuildingDTO
from cookie_clicker.src.app.buildings.domain.providers.i_upgrade_adapter import IBuildingAdapter

class FetchBuildingAdapter(IBuildingAdapter):
    def fetch_building_element(self, driver: Chrome) -> BuildingDTO:
        """
        Fetches one Building from the DOM.
        """
    
    def fetch_all_available_buildings(self, driver: Chrome) -> list[BuildingDTO]:
        # Not finished yet. 
            # Currently, this returns a list of str which contains each available product's ID. 
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
    
    def __cookies_per_second_tooltip_handler():
        pass