from abc import ABC, abstractmethod
from app.buildings.domain.dtos.building_dto import BuildingDTO

class IBuildingProvider(ABC):
    @abstractmethod
    def fetch_one(self, upgrade_id: int) -> BuildingDTO:
        """
        Fetches one Building.
        """
        
    @abstractmethod
    def fetch_all(self) -> list[BuildingDTO]:
        """
        Fetches all Buildings.
        """