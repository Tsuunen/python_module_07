from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity

if (__name__ == "__main__"):
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    tournament = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 5, Rarity.RARE, 5, 10, "dragon_001")
    wizard = TournamentCard("Ice Wizard", 5, Rarity.RARE, 1, 1, "wizard_001")
    wizard.rank = 1150
    tournament.register_card(dragon)
    tournament.register_card(wizard)
    print(f"{dragon.name} (ID: {dragon.id})")
    print("- Interfaces:",
          [cls.__name__ for cls in dragon.__class__.__mro__[1:-2]])
    print("- Rating:", dragon.rank)
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")
    print(f"{wizard.name} (ID: {wizard.id})")
    print("- Interfaces:",
          [cls.__name__ for cls in wizard.__class__.__mro__[1:-2]])
    print("- Rating:", wizard.rank)
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")
    print("Creating tournament match...")
    print("Match result:", tournament.create_match("dragon_001", "wizard_001"))
    print("\nTournament Leaderboard:")
    lead = tournament.get_leaderboard()
    for i in range(len(lead)):
        print(
            f"{i + 1}. {lead[i].name} - Rating: {lead[i].rank} \
({lead[i].wins}-{lead[i].losses})")
    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
