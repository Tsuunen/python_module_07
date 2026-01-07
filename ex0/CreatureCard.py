from .Card import Card, Rarity, Type
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack: int,
                 health: int) -> None:
        if health <= 0:
            raise ValueError("Health must be a positive integer")
        if attack <= 0:
            raise ValueError("Attack must be a positive integer")

        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = Type.CREATURE

    def play(self, game_state: Dict) -> Dict:
        return ({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        })

    def get_card_info(self) -> Dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "type": self.type.name,
            "attack": self.attack,
            "health": self.health
        })

    def attack_target(self, target: Card) -> Dict:
        try:
            if (self.health <= 0 or target.health <= 0):
                return ({
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": 0,
                    "combat_resolved": False
                })
        except KeyError:
            return ({
                "attacker": self.name,
                "target": "Not a valid target",
                "damage_dealt": 0,
                "combat_resolved": False
            })

        return ({
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        })
