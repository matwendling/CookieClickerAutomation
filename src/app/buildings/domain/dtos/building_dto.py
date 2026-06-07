from dataclasses import dataclass

@dataclass
class BuildingDTO:
    id: str
    name: str
    price: int
    cookies_per_second: int