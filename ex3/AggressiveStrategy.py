from .GameStrategy import GameStrategy
from typing import Dict, List
from ex0.Card import Type
from random import choice
from ex1.SpellCard import EffectType


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        if (not len(hand) or not len(battlefield)):
            return ({
                'cards_played': [],
                'mana_used': 0,
                'targets_attacked': [],
                'damage_dealt': 0
            })
        targets = self.prioritize_targets(battlefield)
        crea = [c for c in hand if c.type == Type.CREATURE]
        spell = [c for c in hand if c.type ==
                 Type.SPELL and c.effect_type == EffectType.DAMAGE]
        cards_played = []
        if (crea):
            cards_played.append(choice(crea))
        if (spell):
            cards_played.append(choice(spell))
        damage = 0
        for c in cards_played:
            if (c.type == Type.CREATURE):
                damage += c.attack
            else:
                damage += 3
        return ({
            'cards_played': [c.name for c in cards_played],
            'mana_used': sum([c.cost for c in cards_played]),
            'targets_attacked': [t.name for t in targets],
            'damage_dealt': damage
        })

    def get_strategy_name(self) -> str:
        return ("Aggressive Strategy")

    def prioritize_targets(self, available_targets: List) -> List:
        prio = [t for t in available_targets if t.type == Type.CREATURE]
        if (not len(prio)):
            return (available_targets)
        return (prio)
