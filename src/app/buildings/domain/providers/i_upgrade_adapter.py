from abc import ABC, abstractmethod
from cookie_clicker.src.app.buildings.domain.dtos.building_dto import BuildingDTO

class IBuildingAdapter(ABC):
    @abstractmethod
    def fetch_one(self, upgrade_id: int) -> BuildingDTO:
        """
        Fetches one Building from the DOM.
        """

    def fetch_all(self) -> list[BuildingDTO]:
        """
        Fetches all Buildings from the DOM.
        """