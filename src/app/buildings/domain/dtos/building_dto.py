from dataclasses import dataclass

@dataclass
class BuildingDTO:
    name: str
    cost: int
    available: bool