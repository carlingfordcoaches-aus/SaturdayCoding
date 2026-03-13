# 🚀 Space Station Commander — Python Project Specification

**Format:** Text-based console game  
**Goal:** Manage a space station by gathering resources, completing missions, upgrading systems, and surviving random space events.

---

# 🎯 Learning Outcomes

By the end of this project students will:

- Use **variables, conditionals, loops, and functions**
- Manage **lists, dictionaries, and simple classes**
- Apply **randomness** to simulate events
- Use **file input/output** for saving and loading
- Plan and test code iteratively
- Write and debug **readable, modular programs**

---

# 🧩 Week-by-Week Breakdown

## Week 1 — Git, Welcome & Menu

Set up your GitHub repository and create the main menu system.

Display a title screen and options:

```
[1] Send Exploration Mission
[2] Manage Crew
[3] Check Station Status
[4] End Day
[Q] Quit Game
```

Requirements:

- Program loops until valid input is entered
- Each option runs the correct action (placeholder functions allowed)

**Milestone:** Menu options behave correctly.

---

# Week 2 — Game State & Day System

Track important game data and loop through days.

Example state dictionary:

```python
state = {
    "day": 1,
    "energy": 100,
    "credits": 50,
    "crew": 3,
    "resources": {
        "metal": 0,
        "fuel": 0,
        "crystals": 0
    }
}
```

Add an **end_day() function** that:

- Increases the day counter
- Consumes a small amount of energy
- Displays updated station status

**Milestone:** Day and resource values update correctly.

---

# Week 3 — Exploration Missions

Players can send missions to gather resources.

Example missions:

- Asteroid Mining
- Planet Scan
- Abandoned Ship Search

Use `random` to generate mission outcomes:

Possible results:

- Gain metal
- Gain fuel
- Gain crystals
- Nothing found
- Ship damaged

Example idea:

```python
import random

outcome = random.choice(["metal", "fuel", "nothing", "damage"])
```

**Milestone:** Missions change the player's resources.

---

# Week 4 — Trading System

Introduce a **space trader** that allows buying and selling.

Example shop items:

```python
shop = {
    "fuel": 10,
    "repair_kit": 15,
    "sensor": 25
}
```

Players can:

- Buy items using credits
- Sell extra resources for profit

Make sure to check if the player **has enough credits**.

**Milestone:** Credits and resources update correctly.

---

# Week 5 — Random Space Events

Add random events that occur at the end of each day.

Example events:

- Solar Flare → Lose energy
- Alien Trader → Discount prices next day
- Meteor Shower → Lose resources
- Supply Drop → Gain free resources

Example:

```
⚠ Solar Flare! The station loses 20 energy.
```

Use:

```python
random.randint()
random.choice()
```

**Milestone:** Events occasionally trigger and affect the game state.

---

# Week 6 — Saving & Loading

Allow players to save and load their game progress.

Use the **json module**.

Functions to create:

```python
save_game()
load_game()
```

Menu additions:

```
[S] Save Game
[L] Load Game
```

Example:

```python
import json
```

**Milestone:** Game loads with the same data after restarting.

---

# Week 7 — Station Upgrades

Allow players to upgrade the space station.

Example upgrades:

- Solar Panels → More energy each day
- Mining Drones → Better mission rewards
- Defense System → Reduces damage from events

Example structure:

```python
upgrades = {
    "solar_panels": 0,
    "mining_drones": 0,
    "defense_system": 0
}
```

**Milestone:** Upgrades affect gameplay.

---

# Week 8 — Refactoring & Functions

Improve code structure and reuse.

Break large code sections into functions such as:

```python
send_mission()
trade_menu()
trigger_event()
end_day()
display_status()
```

Optional challenge:

Create a **Mission class** or **Station class**.

**Milestone:** Code is organized and easier to read.

---

# Week 9 — Difficulty & Game Balance

Add difficulty levels:

- Easy
- Normal
- Hard

Difficulty can change:

- Event frequency
- Resource rewards
- Energy costs

Win / Lose conditions:

```
Win: Reach 500 credits before Day 20
Lose: Energy reaches 0
```

**Milestone:** The game can be won or lost.

---

# Week 10 — Polishing & Reflection

Final improvements:

Add:

- Help screen
- Clear prompts
- Code comments
- Cleaner menu formatting

Students write a **5–8 sentence reflection** about:

- What was hardest
- What was most fun
- What they would add next

**Milestone:** Finished and playable game.

---

# ✅ Weekly Checklist

Each week confirm:

```
[ ] Program runs without crashing
[ ] Weekly feature works
[ ] At least one commit made to GitHub
[ ] Code pushed to repository
```

---

# ⭐ Optional Extension Ideas

Students who finish early can add:

- Alien diplomacy system
- Multiple ships
- Crew leveling system
- Rare artifacts
- Pirate attacks
- Story missions

---

**Good luck Commander 🚀**
