from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory

if (__name__ == "__main__"):
    print("\n=== DataDeck Game Engine ===\n")
    game = GameEngine()
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strat = AggressiveStrategy()
    print("Factory:", type(factory).__name__)
    print("Strategy:", type(strat).__name__)
    print("Available types:", factory.get_supported_types())
    game.configure_engine(factory, strat)
    deck = factory.create_themed_deck(3)
    game.battlefield.append(factory.create_creature("Enemy Player"))
    game.battlefield.append(factory.create_spell("Enemy Spell"))
    for lst in deck.values():
        game.hand.extend(lst)
    print("\nSimulating aggressive turn...")
    print("Hand: [", end="")
    for i in range(len(game.hand)):
        print(f"{game.hand[i].name} ({game.hand[i].cost})", end="")
        if (i < len(game.hand) - 1):
            print(", ", end="")
    print("]\n")
    print("Turn execution:")
    print("Strategy:", type(game.strategy).__name__)
    print("Actions:", game.simulate_turn())
    print("\nGame Report:")
    print(game.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility \
achieved!")
