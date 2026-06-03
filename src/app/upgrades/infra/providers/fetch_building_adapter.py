from cookie_clicker.src.app.upgrades.domain.dtos.upgrade_dto import UpgradeDTO
from cookie_clicker.src.app.upgrades.domain.providers.i_upgrade_adapter import IUpgradeAdapter

class UpgradeAdapter(IUpgradeAdapter):
    def fetch_one(self, Upgrade_id: int) -> UpgradeDTO:
        """
        Fetches one Upgrade from the DOM.
        """

    def fetch_all(self) -> list[UpgradeDTO]:
        """
        Fetches all Upgrades from the DOM.
        """