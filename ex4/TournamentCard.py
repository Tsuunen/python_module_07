from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from .Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: Rarity, damage: int,
                 defense: int, id: str) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense)
        Rankable.__init__(self)
        self.id = id

    def play(self, game_state: Dict) -> Dict:
        return (self.defend(game_state["incoming_damage"]))

    def attack(self, target) -> Dict:
        return ({
            'attacker': self.name,
            'target': target.name,
            'damage': self.damage,
            'combat_type': 'melee'
        })

    def defend(self, incoming_damage: int) -> Dict:
        still_alive = self.defense > incoming_damage
        return ({
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.defense,
            'still_alive': still_alive
        })

    def get_combat_stats(self) -> Dict:
        return ({
            "damage": self.damage,
            "block": self.defense
        })

    def calculate_rating(self) -> int:
        rel = self.wins - self.losses
        return (self.rank + (rel * 16))

    def update_wins(self, wins: int) -> None:
        if (wins >= 0):
            self.wins = wins

    def update_losses(self, losses: int) -> None:
        if (losses >= 0):
            self.losses = losses

    def get_rank_info(self) -> Dict:
        return ({
            "rank": self.rank,
            "wins": self.wins,
            "losses": self.losses
        })
