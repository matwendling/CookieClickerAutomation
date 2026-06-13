from abc import ABC, abstractmethod

from undetected_chromedriver import Chrome
from app.upgrades.domain.dtos.upgrade_dto import UpgradeDTO


class IUpgradeProvider(ABC):
    @abstractmethod
    def fetch_building_element(self, driver: Chrome) -> UpgradeDTO:
        """
        Fetches one Upgrade from the DOM.
        """

    def fetch_all_available_buildings(self, driver: Chrome) -> list[UpgradeDTO]:
        """
        Fetches all Upgrades from the DOM.
        """