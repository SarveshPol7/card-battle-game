import random

class Card:
    def __init__(self, name, kind, amount):
        self.name = name
        self.kind = kind  # 'attack', 'defend', 'heal'
        self.amount = amount

    def __str__(self):
        return f"{self.name} ({self.kind} - {self.amount})"
