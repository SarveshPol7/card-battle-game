# 🃏 Card Battle Game

**Author:** Sarvesh Pol  
**Type:** Individual Project (Self-contained)  
**Course:** Programming Paradigms  

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

## 🧱 File Structure
card-battle-game/
│
├── game.py       → Main entry point and overall game loop
├── battle.py     → Handles player/enemy turn logic and card effects
├── player.py     → Player class (health, shield, hand, deck management)
├── card.py       → Card class (types: attack, defend, heal)
└── README.md     → Project documentation

