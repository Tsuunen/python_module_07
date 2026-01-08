from .EliteCard import EliteCard
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard

if (__name__ == "__main__"):
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    war = EliteCard("Arcane Warrior", 8, Rarity.EPIC, 5, 3)
    en = CreatureCard("Enemy", 1, Rarity.COMMON, 1, 2)
    en1 = CreatureCard("Enemy1", 1, Rarity.COMMON, 1, 2)
    en2 = CreatureCard("Enemy2", 1, Rarity.COMMON, 1, 2)
    print(f"Playing {war.name} ({type(war).__name__}):\n")
    game = {
        "combat_target": en,
        "incoming_damage": 2,
        "spell_name": "Fireball",
        "magic_targets": [en1, en2],
        "channel_mana": 3
    }
    war.play(game)
    print("\nMultiple interface implementation successful!")
