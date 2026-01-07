from ex0.Card import Card, Rarity, Type
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = Type.ARTIFACT

    def play(self, game_state: Dict) -> Dict:
        if (not self.is_playable(game_state["mana_left"])):
            return ({
                "card_played": None,
                "mana_used": 0,
                "effect": None
            })
        self.activate_ability()
        return ({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        })

    def activate_ability(self) -> Dict:
        return ({"effect": self.effect})
