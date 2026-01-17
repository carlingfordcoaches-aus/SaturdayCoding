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
    randomevents = random.randint(1, 100)

    if randomevents == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24:
        print("A merchant arrives and gives you 15 herbs!")
        add_item(state["inventory"], "Herb", 15)
    elif randomevents == 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48:
        print("A bandit steals 15 gold from you!")
        state["gold"] -= 15
    elif randomevents == 49 or 50 or 51 or 52 or 53 or 54 or 55 or 56 or 57 or 58 or 59 or 60 or 61 or 62 or 63 or 64 or 65 or 66 or 67 or 68 or 69 or 70 or 71 or 72:
        print("You found a hidden stash of 50 gold!")
        state["gold"] += 50
    elif randomevents == 73 or 74 or 75 or 76 or 77 or 78 or 79 or 80 or 81 or 82:
        print("You found a treasure chest with 2 helmets.")
        add_item(state["inventory"], "Helmet", 2)
    elif randomevents == 97 or 98 or 99 or 100:
        print("A traveling blacksmith gives you a legendary sword!")
        add_item(state["inventory"], "Legendary Sword", 1)
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
    "Magic Scroll": {"buy": 5000000000, "sell": 7000000000},
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