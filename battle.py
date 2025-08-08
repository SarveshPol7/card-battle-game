import asyncio
import random

def apply_card_effect(card, user, target):
    if card.kind == 'attack':
        print(f"{user.name} deals {card.amount} damage!")
        target.take_damage(card.amount)
    elif card.kind == 'defend':
        print(f"{user.name} gains {card.amount} shield!")
        user.shield += card.amount
    elif card.kind == 'heal':
        print(f"{user.name} heals {card.amount} HP!")
        user.hp = min(100, user.hp + card.amount)

async def player_turn(player, opponent):
    print(f"\n{player.name} HP: {player.hp}, Shield: {player.shield}")
    print(f"{opponent.name} HP: {opponent.hp}")

    print("Your cards:")
    for idx, c in enumerate(player.hand):
        print(f"{idx + 1}. {c}")

    while True:
        try:
            selection = int(input(f"Select a card (1-{len(player.hand)}): ")) - 1
            if 0 <= selection < len(player.hand):
                break
            else:
                print("❗ Invalid input. Try again.")
        except ValueError:
            print("❗ Please input a number.")

    selected_card = player.play_card(selection)
    if selected_card:
        print(f"\nYou chose: {selected_card}")
        apply_card_effect(selected_card, player, opponent)
        player.draw_card()
    await asyncio.sleep(1)

async def enemy_turn(enemy, player):
    card = random.choice(enemy.hand)
    enemy.hand.remove(card)
    print(f"\n{enemy.name} uses {card}")
    apply_card_effect(card, enemy, player)
    enemy.draw_card()
    await asyncio.sleep(1)
