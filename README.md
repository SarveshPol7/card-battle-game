# 🃏 Card Battle Game

**Author:** Sarvesh Pol  
**Type:** Individual Project   
**Course:** Programming Languages CS3003
---

## 🎯 Project Overview
This is a **coroutine-based, turn-based card battle game** written in Python.  
It applies **asynchronous programming** using `asyncio` for turn sequencing, and **object-oriented principles** for structuring game components (`Player` and `Card` classes).  

The project is **modular** with separate files for the main game loop, battle logic, player state, and card definitions.

---

## 📚 Course Concepts Applied
- **Asynchronous Programming:** Player and enemy turns are handled as coroutines (`async def` / `await`).
- **Object-Oriented Design:** Encapsulation of player state, card attributes, and methods.
- **Modular Code Organization:** Game split into multiple `.py` files for clarity and maintainability.
- **CLI-based User Interaction:** Validated user input for card selection.

---

## 🎥 Video Walkthrough

- [📽 Video Walkthrough 1](ADD_LINK_HERE_1) — Demonstrates gameplay, explains code structure, and connects to course concepts.  
- [📽 Video Walkthrough 2](ADD_LINK_HERE_2) — Demonstrates gameplay, explains code structure, and connects to course concepts.


## 🧱 File Structure
card-battle-game/
│
├── game.py       → Main entry point and overall game loop
├── battle.py     → Handles player/enemy turn logic and card effects
├── player.py     → Player class (health, shield, hand, deck management)
├── card.py       → Card class (types: attack, defend, heal)
└── README.md     → Project documentation


## 🎮 How to Play

1. **On your turn**, choose a card by entering its number.

### Card Types
- 🗡 **Attack** → Damage the opponent.
- 🛡 **Defend** → Gain shield for one turn.
- 💊 **Heal** → Recover HP.

2. **Enemy Turn** → The enemy plays randomly.

3. **Win Condition** → The first player to reach **0 HP** loses.






