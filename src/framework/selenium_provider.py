import os
import undetected_chromedriver as uc

class UndetectedChromedriverProvider:
    def __init__(self):
        driver_version = os.getenv('UNDETECTED_CHROMEDRIVER_V')
        driver = uc.Chrome(version_main=int(driver_version))

        self.driver = driver

    def get_all_buildings_DOM():
        pass

    def get_all_upgrades_DOM():
        pass

    def get_cookie_count_DOM():
        pass