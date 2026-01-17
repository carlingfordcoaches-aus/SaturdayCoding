"""
Quest Shop — Starter Code
Author: <Student Name>
Week: 1–2

This is the starter code for your Quest Shop game.
You’ll expand this each week by adding new features.
"""

# === Imports ===
import random
import json

# === Helper Functions ===
def show_status(state):
    """Display the current day, gold, and inventory."""
    print(f"\n📅 Day {state['day']} | 💰 Gold: {state['gold']}")
    if not state["inventory"]:
        print("🧺 Inventory: (empty)")
    else:
        print("🧺 Inventory:")
        for item, qty in state["inventory"].items():
            print(f"   {item} x{qty}")


def add_item(inv, name, qty):
    """Add items to the player’s inventory."""
    inv[name] = inv.get(name, 0) + qty


def can_afford(state, cost):
    """Check if player can afford an item."""
    return state["gold"] >= cost

def randomEvent(state):
    randomevents = random.randint(1, 4)

    if randomevents == 1:
        print("A merchant arrives and gives you 15 herbs!")
        add_item(state["inventory"], "Herb", 15)
    elif randomevents == 2:
        print("A bandit steals 15 gold from you!")
        state["gold"] -= 15
    elif randomevents == 3:
        print("You found a hidden stash of 50 gold!")
        state["gold"] += 50
    else:
        print("Nothing happened today")

# === Game Actions ===
def buy_flow(state):
    """Allow the player to buy items."""
    print("\n=== 🛒 BUY ITEMS ===")
    for i, (name, data) in enumerate(CATALOG.items(), start=1):
        print(f"[{i}] {name} (buy {data['buy']}g)")
    print("[0] Back")

    choice = input("> ").strip()
    if choice == "0":
        return

    try:
        idx = int(choice) - 1
        item_name = list(CATALOG.keys())[idx]
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")
        return

    try:
        qty = int(input("How many would you like to buy? "))
        if qty <= 0:
            print("⚠️ Quantity must be positive.")
            return
    except ValueError:
        print("⚠️ Please enter a number.")
        return

    cost = CATALOG[item_name]["buy"] * qty
    if not can_afford(state, cost):
        print("❌ Not enough gold.")
        return

    state["gold"] -= cost
    add_item(state["inventory"], item_name, qty)
    print(f"✅ Bought {qty} {item_name}(s) for {cost} gold.")


def sell_to_customer(state):
    """Sell random items to a customer."""
    print("\n=== 💬 CUSTOMER ===")
    item = random.choice(list(CATALOG.keys()))
    qty = random.randint(1, 3)
    price = CATALOG[item]["sell"] * qty
    print(f"A customer wants {qty} {item}(s) for {price} gold.")

    have = state["inventory"].get(item, 0)
    if have >= qty:
        state["inventory"][item] -= qty
        state["gold"] += price
        print("✅ Sale complete!")
    else:
        print("😞 You don’t have enough. The customer leaves.")


def end_day(state):
    """End the day and move to the next one."""
    print("\n🌙 The day ends...")
    state["day"] += 1
    print(f"🌞 It is now Day {state['day']}.")


def save_game(state):
    try:
        with open('main_save.json', 'w') as f:
            json.dump(state, f, indent=2)
        print("✅ Game saved successfully.")
    except Exception as e:
        print(f"❌ Error saving game: {e}")


def load_game():
    try:
        with open('main_save.json', 'r') as f:
            data = json.load(f)
        print("✅ Game loaded successfully.")
        return data
    except FileNotFoundError:
        print("❌ No save file found.")
        return None
    except Exception as e:
        print(f"❌ Error loading game: {e}")
        return None


# === Game Setup ===
CATALOG = {
    "Herb": {"buy": 3, "sell": 4},
    "Potion": {"buy": 5, "sell": 7},
    "Sword": {"buy": 20, "sell": 28},
    "Axe": {"buy": 50, "sell": 75},
    "Helmet": {"buy": 200, "sell": 300},
    "Bow": {"buy": 1000, "sell": 1500},
    "Shield": {"buy": 5000, "sell": 7500},
    "Amour": {"buy": 20000, "sell": 30000},
    "Horse": {"buy": 100000, "sell": 150000},
    "Carriage": {"buy": 5000000, "sell": 7500000},
    "Castle": {"buy": 150000000, "sell": 210000000},
    "Magic Scroll": {"buy": 5000000000, "sell": 7000000000},
    "Diamond": {"buy": 1000000000000, "sell": 3000000000000},
    "Legendary Sword": {"buy": 50000000000000, "sell": 75000000000000},
}


def new_game():
    # Create a new game state with starting values
    return {
        "day": 1,
        "gold": 50,
        "inventory": {},
    }




# === Main Loop ===
def day_menu(state):
    # Main daily menu for the player
    while True:
        show_status(state)
        print('[1] Buy Items  [2] Sell to Customer  [3] End Day [4] Craft Items [L] Load Game [S] Save Game [Q] Quit Game')
        option = input('> ')
        if option == '1':
            buy_flow(state)
        elif option == '2':
            sell_to_customer(state)
        elif option == '3':
            randomEvent(state)
            end_day(state)
            return
        elif option == '4':
            craft_items()
        elif option == 'Q':
            print('Goodbye!')
            raise SystemExit(0)
        elif option == 'S':
            save_game(state)
        elif option == 'L':
            loaded = load_game()
            if loaded:
                state.clear()
                state.update(loaded)
                print("✅ Game state updated from save file.")
        else:
            print('⚠️ Invalid option.')


def main():
    """Run the Quest Shop game."""
    while True:
        day_menu(state)


# === Program Start ===
if __name__ == "__main__":
    print("🏰 Welcome to QUEST SHOP")
    state = new_game()
    main()

def craft_items():
    """Allow the player to craft items."""
    print("\n=== 🛠️ CRAFT ITEMS ===")
    print("Available recipes:")
    print("[1] Potion (requires 5 Herbs) - sells for 7g")
    print("[0] Back")

    choice = input("> ")
    if choice == "0":
        return

    if choice == "1":
        have_herbs = state["inventory"].get("Herb", 0)
        if have_herbs >= 5:
            state["inventory"]["Herb"] -= 5
            add_item(state["inventory"], "Potion", 1)
            print("✅ Crafted 1 Potion.")
        else:
            print("❌ Not enough Herbs to craft a Potion.")
    else:
        print("⚠️ Invalid choice.")