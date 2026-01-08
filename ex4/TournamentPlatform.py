from .TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform():
    def __init__(self):
        self.cards = []
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if (not isinstance(card, TournamentCard)):
            return ("Card not registered")
        self.cards.append(card)
        return ("Card successfully registered")

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        attack = [c for c in self.cards if c.id == card1_id]
        defense = [c for c in self.cards if c.id == card2_id]
        if (not len(attack) or not len(defense)):
            return ({})
        attack = attack[0]
        defense = defense[0]
        result = defense.play({"incoming_damage": attack.damage})
        if (result["still_alive"]):
            winner = defense
            loser = attack
        else:
            winner = attack
            loser = defense
        winner.wins += 1
        loser.losses += 1
        self.match_played += 1
        return ({
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        })

    def get_leaderboard(self) -> List:
        return (sorted(self.cards, key=lambda c: c.rank, reverse=True))

    def generate_tournament_report(self) -> Dict:
        total_cards = len(self.cards)
        if (total_cards == 0):
            avg = 0
        else:
            avg = sum([c.rank for c in self.cards]) / total_cards
        return ({
            'total_cards': total_cards,
            'matches_played': self.match_played,
            'avg_rating': avg,
            'platform_status': 'active'
        })
