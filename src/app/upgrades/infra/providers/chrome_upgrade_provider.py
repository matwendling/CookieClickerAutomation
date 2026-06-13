from app.upgrades.domain.dtos.upgrade_dto import UpgradeDTO
from app.upgrades.domain.providers.i_upgrade_adapter import IUpgradeProvider

class UpgradeAdapter(IUpgradeProvider):
    def fetch_one(self, Upgrade_id: int) -> UpgradeDTO:
        """
        Fetches one Upgrade from the DOM.
        """

    def fetch_all(self) -> list[UpgradeDTO]:
        """
        Fetches all Upgrades from the DOM.
        """