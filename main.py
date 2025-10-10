"""
Quest Shop — Starter Code
Author: <Student Name>
Week: 1–2

This is the starter code for your Quest Shop game.
You’ll expand this each week by adding new features.
"""

# === Imports ===
import random

# === Game Setup ===
CATALOG = {
    "Herb": {"buy": 3, "sell": 4},
    "Potion": {"buy": 5, "sell": 7},
    "Sword": {"buy": 20, "sell": 28},
}


def new_game():
    """Create a new game state with starting values."""
    return {
        "day": 1,
        "gold": 50,
        "inventory": {},
    }


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


# === Main Loop ===
def day_menu(state):
    """Main daily menu for the player."""
    while True:
        show_status(state)
        """Write your week 1 code in here!!!"""


def main():
    """Run the Quest Shop game."""
    print("🏰 Welcome to QUEST SHOP!")
    state = new_game()

    while True:
        day_menu(state)


# === Program Start ===
if __name__ == "__main__":
    main()
