from app.buildings.domain.dtos.building_dto import BuildingDTO
from app.buildings.domain.providers.i_building_provider import IBuildingProvider


class GetBestAvailableBuilding:
    def __init__(
            self, building_provider: IBuildingProvider
            ):
            self.building_provider = building_provider

    def execute(self):
        available_buildings = []
        best_building = 0
        # for building in available_buildings:
        #     if building[""]