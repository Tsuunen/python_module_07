from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from .SpellCard import SpellCard, EffectType
from .ArtifactCard import ArtifactCard

if (__name__ == "__main__"):
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck: Deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3,
                  Rarity.RARE, EffectType.DAMAGE))
    deck.add_card(ArtifactCard("Mana Crystal", 4,
                  Rarity.COMMON, 4, "Permanent: +1 mana per turn"))
    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:\n")
    gob = CreatureCard("Gobelin Warrior", 1, Rarity.COMMON, 2, 3)
    game = {
        "target": gob,
        "targets": [gob],
        "mana_left": 100
    }
    deck.shuffle()
    while (len(deck.cards)):
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type.name})")
        print("Play result:", card.play(game))
        print()

print("\nPolymorphism in action: Same interface, different card behaviors!")
