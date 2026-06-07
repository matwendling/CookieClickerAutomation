from dataclasses import dataclass

@dataclass
class UpgradeDTO:
    id: str
    name: str
    price: int
    cookies_per_second: int