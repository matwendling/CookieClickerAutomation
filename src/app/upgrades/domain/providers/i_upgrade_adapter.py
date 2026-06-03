from abc import ABC, abstractmethod
from cookie_clicker.src.app.upgrades.domain.dtos.upgrade_dto import UpgradeDTO

class IUpgradeAdapter(ABC):
    @abstractmethod
    def fetch_one(self, upgrade_id: int) -> UpgradeDTO:
        """
        Fetches one Upgrade from the DOM.
        """

    def fetch_all(self) -> list[UpgradeDTO]:
        """
        Fetches all Upgrades from the DOM.
        """