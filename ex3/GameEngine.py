from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from typing import Dict


class GameEngine():
    def __init__(self):
        self.strategy = None
        self.factory = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.damage_dealt = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if (self.strategy is None):
            return ({})
        turn = self.strategy.execute_turn(self.hand, self.battlefield)
        self.damage_dealt += turn["damage_dealt"]
        self.turns_simulated += 1
        return (turn)

    def get_engine_status(self) -> Dict:
        return ({
            'turns_simulated': self.turns_simulated,
            'strategy_used': type(self.strategy).__name__,
            'total_damage': self.damage_dealt,
            'cards_created': len(self.hand)
        })
