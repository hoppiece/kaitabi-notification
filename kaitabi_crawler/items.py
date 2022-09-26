from dataclasses import dataclass


@dataclass
class KaitabiCrawlerItem:
    name: str
    date: str
    vacancy: int
    reservation_url: str
