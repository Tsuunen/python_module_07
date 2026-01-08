from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    def __init__(self, attack, defense):
        self.damage = attack
        self.defense = defense

    @abstractmethod
    def attack(self, target) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
