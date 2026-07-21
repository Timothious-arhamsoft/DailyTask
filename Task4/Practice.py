# Data Classes
from dataclasses import dataclass, field
from math import asin, cos, radians, sin, sqrt
import pytest
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
print(oslo.distance_to(vancouver))


from typing import List
# Creating Deck
@dataclass
class Playcard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[Playcard]

queen_of_hearts = Playcard("Q", "Hearts")
ace_of_spades = Playcard("A", "Spades")
King_of_hearts = Playcard("K", "Hearts")

cards = Deck([queen_of_hearts, King_of_hearts, ace_of_spades])

print(cards)


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def create_deck():
    return [Playcard(r,s) for s in SUITS for r in RANKS]

print("Deck: ",create_deck())

@dataclass
class Deck_v2:
    cards: List[Playcard] = field(default_factory=create_deck)
print("Deck V2: ")
print(Deck_v2())


# Parameterized test
@pytest.mark.parametrize(
    "a,b,result",
    [
        (1,2,3),
        (3,5,8),
        (4,7,11)
    ]
)
def test_add(a,b, result):
    assert a+b == result


