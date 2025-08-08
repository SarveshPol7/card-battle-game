import random

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hp = 100
        self.shield = 0
        self.deck = deck[:]
        self.hand = random.sample(self.deck, 3)

    def draw_card(self):
        card = random.choice(self.deck)
        self.hand.append(card)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        return None

    def take_damage(self, damage):
        reduced = max(0, damage - self.shield)
        self.hp -= reduced
        self.shield = 0
