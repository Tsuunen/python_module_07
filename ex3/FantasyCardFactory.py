from .CardFactory import CardFactory
from ex0.Card import Card, Rarity
from typing import Dict
from ex0.CreatureCard import CreatureCard
from random import randint, choice
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.types = {
            'creatures': ['Dragon', 'Goblin', "Elve", "Dwarf", "Human"],
            'spells': ['Fireball', 'Lightnigh Bolt', 'Ice Arrow'],
            'artifacts': ['Mana Ring'],
            'types': ["Fire", "Ice", "Warrior"]
        }

    def create_creature(self, name_or_power) -> Card:
        return (CreatureCard(name_or_power, randint(1, 10),
                             choice(list(Rarity)),
                             randint(2, 15), randint(2, 15)))

    def create_spell(self, name_or_power) -> Card:
        return (SpellCard(name_or_power, randint(1, 10),
                          choice(list(Rarity)), choice(list(EffectType))))

    def create_artifact(self, name_or_power) -> Card:
        return (ArtifactCard(name_or_power, randint(1, 10),
                             choice(list(Rarity)), "+1 permanent mana"))

    def create_themed_deck(self, size: int) -> Dict:
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        for i in range(size):
            if (i <= size / 2):
                deck["creatures"].append(self.create_creature(
                    choice(self.types["types"]) +
                    choice(self.types["creatures"])
                ))
            elif (i <= size / 2 + size / 4):
                deck["spells"].append(self.create_spell(
                    choice(self.types["spells"])
                ))
            else:
                deck["artifacts"].append(self.create_spell(
                    choice(self.types["artifacts"])
                ))
        return (deck)

    def get_supported_types(self) -> Dict:
        return (self.types)
