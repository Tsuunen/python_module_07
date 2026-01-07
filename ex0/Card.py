from enum import Enum
from typing import Dict
from abc import ABC, abstractmethod


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


class Type(Enum):
    CREATURE = 0
    SPELL = 1
    ARTIFACT = 2


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name
        })

    def is_playable(self, available_mana: int) -> bool:
        if (available_mana >= self.cost):
            return (True)
        return (False)
