from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.rank = 1200

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        pass
