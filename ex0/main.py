from .CreatureCard import CreatureCard
from .Card import Rarity

if (__name__ == "__main__"):
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play({}))
    print("\nFire Dragon attacks Goblin Warrior:")
    gob = CreatureCard("Gobelin Warrior", 1, Rarity.COMMON, 2, 3)
    print("Attack result:", dragon.attack_target(gob))
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")
