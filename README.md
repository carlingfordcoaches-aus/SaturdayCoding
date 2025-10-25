
# 🧙‍♂️ Quest Shop — Branson's Python Project Specification

**Format:** Text-based console game  
**Goal:** Build a shop simulation game where the player buys items, sells to adventurers, crafts goods, and survives random events.

## Email for help: 
aarya.dave123@gmail.com

---

## 🎯 Learning Outcomes
By the end of the project, students will:
- Use variables, conditionals, loops, and functions  
- Manage lists, dictionaries, and simple classes  
- Apply randomness to simulate events  
- Use file input/output for saving and loading  
- Plan and test code iteratively  
- Write and debug readable, modular programs

---

## 🧩 Week-by-Week Breakdown (Ask me [Aarya] for any help if you need)

### Week 1 — GIT, Welcome & Menu
Get your github stuff fully setup and working!!!
Display a main menu and handle user input.  
- Title screen and options `[1] Buy Items  [2] Sell to Customer  [3] End Day [Q] Quit Game`  
- Loops until valid input is chosen  
- Perform an appropriate action once a specific one has been chosen
**Milestone:** Menu options behave correctly.

### Week 2 — Game State & Day System
Track basic game data and loop through days.  
- `state` dict with `day`, `gold`, `inventory`  
- End-of-day function increments day  
**Milestone:** Day and gold values update correctly.
```Python
dict = {
    "item1": 10,
    "item2": 15,
    "item3": 20,
}

```

---

### Week 3 — Buying Items
Introduce an item catalogue and buying system.  
- Hard-coded items (Potion, Herb, Sword)  
- Buy items using gold; validate affordability  
**Milestone:** Inventory and gold adjust accurately.

---

### Week 4 — Customers & Selling
Create random customers who request items.  
- Random item + quantity  
- Sell for profit if in stock  
**Milestone:** Sales update inventory and gold.

---

### Week 5 — Daily Events
Add random daily events.  
- Examples: “Bandits”, “Market Sale”, “Free Herbs”  
- Events affect gold, inventory, or next day’s prices  
**Milestone:** Events trigger occasionally and change the state.

---

### Week 6 — Saving & Loading
Allow saving progress with JSON.  
- `save_game()` and `load_game()` using `json`  
- Add `[S] Save` and `[L] Load` to menu  
**Milestone:** Game reloads with same data after restart.

---

### Week 7 — Crafting System
Combine items into new products.  
- Recipes (e.g. 2 Herbs → 1 Potion)  
- Checks inventory before crafting  
**Milestone:** Crafting consumes ingredients and adds result.

---

### Week 8 — Refactor & Functions
Improve structure and reuse code.  
- Modular functions (`buy_flow`, `sell_to_customer`, `end_day`)  
- Optional small `Item` class  
**Milestone:** Code is organised into logical parts.

---

### Week 9 — Difficulty & Balancing
Add challenge and victory conditions.  
- Difficulty modes (Easy/Normal/Hard)  
- Lose if gold < 0; win if gold ≥ 200 by Day 14  
**Milestone:** Game can be won or lost.

---

### Week 10 — Polishing & Reflection
Clean up and reflect.  
- Help screen, clear prompts, comments  
- 5–8 sentence reflection: what was hardest, most fun, what to add next  
**Milestone:** Finished, working game with reflection.

---
---

### Weekly Check (2–3 min)
- [] Runs without crashing  
- [] Weekly feature works  
- [] At least one commit made to github, and one push of working code!

---

