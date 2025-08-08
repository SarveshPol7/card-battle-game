import asyncio
from card import Card
from player import Player
from battle import player_turn, enemy_turn

def create_deck():
    return [
        Card("Strike", "attack", 20),
        Card("Block", "defend", 15),
        Card("Heal", "heal", 10),
        Card("Heavy Slash", "attack", 30),
        Card("Shield Wall", "defend", 25)
    ]

async def game_loop():
    hero = Player("Hero", create_deck())
    goblin = Player("Goblin", create_deck())

    print("⚔️ Card Battle Starts!")
    while hero.hp > 0 and goblin.hp > 0:
        await player_turn(hero, goblin)
        if goblin.hp <= 0:
            print("🏆 You win!")
            break

        await enemy_turn(goblin, hero)
        if hero.hp <= 0:
            print("💀 You lose!")
            break

if __name__ == "__main__":
    asyncio.run(game_loop())
