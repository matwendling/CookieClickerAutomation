from dataclasses import dataclass

@dataclass
class UpgradeDTO:
    name: str
    cost: int
    available: bool