from ex0.Card import Card, Type
from random import shuffle
from typing import Dict


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        tmp = len(self.cards)
        self.cards = [c for c in self.cards if c.name != card_name]
        if (tmp > len(self.cards)):
            return (True)
        return (False)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return (self.cards.pop(0))

    def get_deck_stats(self) -> Dict:
        if (len(self.cards) == 0):
            avg_cost = 0
        else:
            avg_cost = sum([c.get_card_info()["cost"]
                            for c in self.cards]) / len(self.cards)
        return ({
            "total_cards": len(self.cards),
            "creatures": len([c for c in self.cards
                if c.type == Type.CREATURE]),
            "spells": len([c for c in self.cards
                if c.type == Type.SPELL]),
            "artifacts": len([c for c in self.cards
                if c.type == Type.ARTIFACT]),
            "avg_cost": avg_cost
        })
