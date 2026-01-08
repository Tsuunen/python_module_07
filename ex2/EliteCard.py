from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card, Rarity, Type
from typing import Dict


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity, damage: int,
                 defense: int) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense)
        self.type = Type.CREATURE

    def play(self, game_state: Dict) -> Dict:
        print("Combat Phase:")
        print("Attack result:", self.attack(game_state["combat_target"]))
        print("Defense result:", self.defend(game_state["incoming_damage"]))
        print("\nMagic Phase:")
        print("Spell cast:", self.cast_spell(
            game_state["spell_name"], game_state["magic_targets"]))
        print("Mana channel:", self.channel_mana(game_state["channel_mana"]))

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

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        return ({
            'caster': self.name,
            'spell': spell_name,
            'targets': [t.name for t in targets],
            'mana_used': 4
        })

    def channel_mana(self, amount: int) -> Dict:
        return ({
            'channeled': amount,
            'total_mana': 7
        })

    def get_magic_stats(self) -> Dict:
        return ({
            "mana": 5
        })
