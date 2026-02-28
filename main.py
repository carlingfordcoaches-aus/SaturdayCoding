"""
Quest Shop — Starter Code
Author: <student name>
Week: 1–2

This is the starter code for your Quest Shop game.
You’ll expand this each week by adding new features.
"""

# === Imports ===
from os import system
import random
import json


def main():
    """Run the Quest Shop game."""
    while True:
        print("[1] New Game  [2] Load Game [H] Help [Q] Quit")
        choice = input("> ").strip().lower()
        if choice == "1":
            state = new_game()
            day_menu(state)
        elif choice == "2":
            loaded = load_game()
            if loaded:
                state = loaded
                day_menu(state)
        elif choice == "h" or choice == "H":
            show_help()
        elif choice == "q" or choice == "Q":
            print("Thanks for playing!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")
            main()

# === Game Setup ===


def new_game():
    # Create a new game state with starting values
    difficulty = input("[1] Easy  [2] Normal  [3] Hard\n> ")
    if difficulty == "1":
        return {
            "difficulty": "1",
            "day": 1,
            "gold": 50,
            "inventory": {},
            difficulty: "1"
        }
    elif difficulty == "2":
        return {
            "difficulty": "2",
            "day": 1,
            "gold": 25,
            "inventory": {},
            difficulty: "2"
            
        }
    elif difficulty == "3":
        return {
            "difficulty": "3",
            "day": 1,
            "gold": 10,
            "inventory": {},
            difficulty: "3"
        }
    else:
        print("⚠️ Invalid choice. Please try again.")
        new_game()
    return difficulty


CATALOG = {
    "Herb": {"buy": 5, "sell": 7},
    "Potion": {"buy": 10, "sell": 15},
    "Helmet": {"buy": 100, "sell": 300},
    "Sword": {"buy": 28, "sell": 50},
    "Magic Scroll": {"buy": 7000000, "sell": 10000000},
    "Legendary Scroll": {"buy": 50000000000000, "sell": 75000000000000},
    "Legendary Sword": {"buy": 7500000000000, "sell": 10000000000000}
}

        


# === Helper Functions ===
def show_status(state):
    """Display the current day, gold, and inventory."""
    print(f"\n📅 Day {state['day']}  💰 Gold: {state['gold']} | 💀 Difficulty: {state['difficulty']}")
    if not state["inventory"]:
        print("🧺 Inventory: (empty)")
    else:
        print("🧺 Inventory:")
        for item, qty in state["inventory"].items():
            print(f"   {item} x{qty}")

# === inventory management ===
def add_item(inv, name, qty):
    """Add items to the player’s inventory."""
    inv[name] = inv.get(name, 0) + qty


def can_afford(state, cost):
    """Check if player can afford an item."""
    return state["gold"] >= cost

# === event function ===
def randomEvent():
    
    if state["difficulty"] == "1":
        randomevents = random.randint(1, 80)
        luckyevent = random.randint(1, 10)
        if randomevents == 1 or randomevents == 2 or randomevents == 3 or randomevents == 4 or randomevents == 5 or randomevents == 6 or randomevents == 7 or randomevents == 8 or randomevents == 9 or randomevents == 10:
            print("A merchant arrives and gives you 15 herbs!")
            add_item(state["inventory"], "Herb", 15)
        elif randomevents == 11 or randomevents == 12 or randomevents == 13 or randomevents == 14 or randomevents == 15 or randomevents == 16 or randomevents == 17 or randomevents == 18 or randomevents == 19 or randomevents == 20:
            print("A bandit steals 15 gold from you!")
            state["gold"] -= 15
        elif randomevents == 21 or randomevents == 22 or randomevents == 23 or randomevents == 24 or randomevents == 25 or randomevents == 26 or randomevents == 27 or randomevents == 28 or randomevents == 29 or randomevents == 30:
            print("You found a hidden stash of 50 gold!")
            state["gold"] += 50
        elif randomevents == 31 or randomevents == 32 or randomevents == 33 or randomevents == 34 or randomevents == 35 or randomevents == 47 or randomevents == 48 or randomevents == 49:
            print("You found a treasure chest with 2 helmets.")
            add_item(state["inventory"], "Helmet", 2)
        elif randomevents == 36 or randomevents == 39 or randomevents == 40 or randomevents == 41 or randomevents == 42 or randomevents == 43 or randomevents == 44 or randomevents == 45 or randomevents == 46:
            wonderingBlacksmith()
        elif randomevents == 37 or randomevents == 38:
            print("A sudden storm damages your shop, you lose 20 gold in repairs.")
            if luckyevent == 10:
                print('However, you found a magic scroll in the debris!')
                add_item(state["inventory"], "Magic Scroll", 1)
            state["gold"] -= 20
        else:
            print("Nothing happened today")
    if state["difficulty"] == "2":
        randomevents = random.randint(1, 70)
        luckyevent = random.randint(1, 36)
        if randomevents == 1 or randomevents == 2 or randomevents == 3 or randomevents == 4 or randomevents == 5 or randomevents == 6 or randomevents == 7 or randomevents == 8 or randomevents == 9 or randomevents == 10:
            print("A merchant arrives and gives you 15 herbs!")
            add_item(state["inventory"], "Herb", 15)
        elif randomevents == 11 or randomevents == 12 or randomevents == 13 or randomevents == 14 or randomevents == 15 or randomevents == 16 or randomevents == 17 or randomevents == 18 or randomevents == 19 or randomevents == 20:
            print("A bandit steals 15 gold from you!")
            state["gold"] -= 15
        elif randomevents == 21 or randomevents == 22 or randomevents == 23 or randomevents == 24 or randomevents == 25 or randomevents == 26 or randomevents == 27 or randomevents == 28 or randomevents == 29 or randomevents == 30:
            print("You found a hidden stash of 50 gold!")
            state["gold"] += 50
        elif randomevents == 31 or randomevents == 32 or randomevents == 33 or randomevents == 34 or randomevents == 35 or randomevents:
            print("You found a treasure chest with 2 helmets.")
            add_item(state["inventory"], "Helmet", 2)
        elif randomevents == 36 or randomevents == 39 or randomevents == 40 or randomevents == 41 or randomevents == 42 or randomevents == 43 or randomevents == 44 or randomevents == 45 or randomevents == 46:
            wonderingBlacksmith()
        elif randomevents == 37 or randomevents == 38:
            print("A sudden storm damages your shop, you lose 20 gold in repairs.")
            if luckyevent == 36:
                print('However, you found a magic scroll in the debris!')
                add_item(state["inventory"], "Magic Scroll", 1)
            state["gold"] -= 20
        else:
            print("Nothing happened today")
    if state["difficulty"] == "3":
        randomevents = random.randint(1, 70)
        luckyevent = random.randint(1, 72)
        if randomevents == 1 or randomevents == 2 or randomevents == 3 or randomevents == 4 or randomevents == 5 or randomevents == 6 or randomevents == 7 or randomevents == 8 or randomevents == 9 or randomevents == 10:
            print("A merchant arrives and gives you 15 herbs!")
            add_item(state["inventory"], "Herb", 15)
        elif randomevents == 11 or randomevents == 12 or randomevents == 13 or randomevents == 14 or randomevents == 15 or randomevents == 16 or randomevents == 17 or randomevents == 18 or randomevents == 19 or randomevents == 20:
            print("A bandit steals 15 gold from you!")
            state["gold"] -= 15
        elif randomevents == 21 or randomevents == 22 or randomevents == 23 or randomevents == 24 or randomevents == 25 or randomevents == 26 or randomevents == 27 or randomevents == 28 or randomevents == 29 or randomevents == 30:
            print("You found a hidden stash of 50 gold!")
            state["gold"] += 50
        elif randomevents == 31 or randomevents == 32 or randomevents == 33 or randomevents == 34 or randomevents == 35 or randomevents:
            print("You found a treasure chest with 2 helmets.")
            add_item(state["inventory"], "Helmet", 2)
        elif randomevents == 36 or randomevents == 39 or randomevents == 40 or randomevents == 41 or randomevents == 42 or randomevents == 43 or randomevents == 44 or randomevents == 45 or randomevents == 46:
            wonderingBlacksmith()
        elif randomevents == 37 or randomevents == 38:
            print("A sudden storm damages your shop, you lose 20 gold in repairs.")
            if luckyevent == 36:
                print('However, you found a magic scroll in the debris!')
                add_item(state["inventory"], "Magic Scroll", 1)
            state["gold"] -= 20
        else:
            print("Nothing happened today")

def wonderingBlacksmith():
    legendary = random.randint(1, 64)    
    print("A traveling blacksmith passes your shop")
    if legendary == 32 or legendary == 31:
        print("He gave you a Legendary Sword")
        add_item(state["inventory"], "Legendary Sword", 1)
    else:
        print("He gave you a helmet")
        add_item(state["inventory"], "Helmet", 1)

# === Main Loop ===
def day_menu(state):
    # Main daily menu for the player
    while True:
        show_status(state)
        if state["difficulty"] == "1":
            print("You need 1 billion (1000000000) gold by day 300 to win.")
        elif state["difficulty"] == "2":
            print("You need 1 trillion (1000000000000) gold by day 300 to win.")
        elif state["difficulty"] == "3":
            print("You need 1 quadrillion (1000000000000000) gold by day 300 to win.")
        print('[1] Buy Items  [2] Sell to Customer  [3] End Day [4] Craft Items [H] Help [S] Save Game [Q] Quit Game')
        option = input('> ')
        if option == '1':
            buy_flow(state)
        elif option == '2':
            sell_to_customer(state)
        elif option == '3':
            randomEvent()
            end_day(state)
            return
        elif option == '4':
            craft_items()
        elif option == 'H' or option == 'h':
            show_help()
        elif option == 'Q' or option == 'q':
            print('Goodbye!')
            raise SystemExit(0)
        elif option == 'S' or option == 's':
            save_game(state)
        else:
            print('⚠️ Invalid option.')

def show_help():
    print("\n=== HELP MENU ===")
    print("Welcome to Quest Shop! Here’s how to play:")
    print("- Each day, you can buy items, sell to customers, craft new items, or end the day.")
    print("- Your goal is to reach a certain amount of gold by Day 300 based on your difficulty level.")
    print("- Buying items costs gold, but you can sell them for a profit or use them in crafting.")
    print("- Crafting allows you to combine items into more valuable ones.")
    print("- Random events can help or hinder your progress each day.")
    print("Good luck, and have fun playing Quest Shop!")
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
    elif choice == "8":
        print("⚠️ This item is not available for purchase.")
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

def craft_items():
    """Allow the player to craft items."""
    print("\n=== 🛠️ CRAFT ITEMS ===")
    print("Available recipes:")
    print("[1] Potion (requires 5 Herbs) - sells for 7g")
    print("[2] Helmet (requires 10 Herbs, 1 sword and 100 gold ) - sells for 300g")
    print("[3] Sword (requires 5 Herbs and 10 gold) - sells for 28g")
    print("[4] Magic Scroll (requires 5 Herbs and 5000000 gold) - sells for 7000000g")
    print("[5] Legendary Scroll (requires 4 Magic Scroll, 100 herbs and 3000000000000 gold) - sells for 50000000000000g")
    print("[6] Legendary Sword (requires 1 Legendary Scroll, 1 Sword, and 1000000000 gold) - sells for 7500000000000g")
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
    elif choice == "2":
        have_herbs = state["inventory"].get("Herb", 0)
        have_swords = state["inventory"].get("Sword", 0)
        if have_herbs >= 10 and have_swords >= 1 and state["gold"] >= 100:
            state["inventory"]["Herb"] -= 10
            state["inventory"]["Sword"] -= 1
            state["gold"] -= 100
            add_item(state["inventory"], "Helmet", 1)
            print("✅ Crafted 1 Helmet.")
        else:
            print("❌ Not enough resources to craft a Helmet.")
    elif choice == "3":
        have_herbs = state["inventory"].get("Herb", 0)
        if have_herbs >= 5 and state["gold"] >= 10:
            state["inventory"]["Herb"] -= 5
            state["gold"] -= 10
            add_item(state["inventory"], "Sword", 1)
            print("✅ Crafted 1 Sword.")
        else:
            print("❌ Not enough resources to craft a Sword.")
    elif choice == "4":
        have_herbs = state["inventory"].get("Herb", 0)
        if have_herbs >= 5 and state["gold"] >= 5000000:
            state["inventory"]["Herb"] -= 5
            state["gold"] -= 5000000
            add_item(state["inventory"], "Magic Scroll", 1)
            print("✅ Crafted 1 Magic Scroll.")
        else:
            print("❌ Not enough resources to craft a Magic Scroll.")
    elif choice == "5":
        have_magic_scroll = state["inventory"].get("Magic Scroll", 0)
        have_herbs = state["inventory"].get("Herb", 0)
        if have_magic_scroll >= 4 and state["gold"] >= 3000000000000 and have_herbs >= 100:
            state["inventory"]["Magic Scroll"] -= 4
            state["inventory"]["Herb"] -= 100
            state["gold"] -= 3000000000000
            add_item(state["inventory"], "Legendary Scroll", 1)
            print("✅ Crafted 1 Legendary Scroll.")
        else:
            print("❌ Not enough resources to craft a Legendary Scroll.")
    elif choice == "6":
        have_magic_scroll = state["inventory"].get("Legendary Scroll", 0)
        have_sword = state["inventory"].get("Sword", 0)
        if have_magic_scroll >= 1 and have_sword >= 1 and state["gold"] >= 1000000000:
            state["inventory"]["Legendary Scroll"] -= 1
            state["inventory"]["Sword"] -= 1
            state["gold"] -= 1000000000
            add_item(state["inventory"], "Legendary Sword", 1)
            print("✅ Crafted 1 Legendary Sword.")
        else:
            print("❌ Not enough resources to craft a Legendary Sword.")
    else:
        print("⚠️ Invalid choice.")


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
    if state["day"] == 300:
        if state["difficulty"] == "1":
            dif1(state)
        if state["difficulty"] == "2":
            dif2(state)
        if state["difficulty"] == "3":
            dif3(state)

def dif1(state):
    if state["gold"] >= 1000000000:
        print("🎉 Congratulations! You completed the game on Easy difficulty!")
        print("Would you wish to continue playing? [Y/N]")
        choice = input("> ").strip().lower()
        if choice == "n" or choice == "N":
                raise SystemExit(0)
        if choice == "y" or choice == "Y":
                print("Great! Keep playing and see how much more you can achieve!")
        else:
            print("😞 You did not meet the requirements to complete the game on Easy difficulty.")
            raise SystemExit(0)

def dif2(state):
    if state["gold"] >= 1000000000000:
        print("🎉 Congratulations! You completed the game on Medium difficulty!")
        print("Would you wish to continue playing? [Y/N]")
        choice = input("> ").strip().lower()
        if choice == "n" or choice == "N":
            raise SystemExit(0)
        if choice == "y" or choice == "Y":
            print("Great! Keep playing and see how much more you can achieve!")
    else:
        print("😞 You did not meet the requirements to complete the game on Medium difficulty.")
        raise SystemExit(0)

def dif3(state):
    if state["gold"] >= 1000000000000000:
        print("🎉 Congratulations! You completed the game on Hard difficulty!")
        print("Would you wish to continue playing? [Y/N]")
        choice = input("> ").strip().lower()
        if choice == "n" or choice == "N":
            raise SystemExit(0)
        if choice == "y" or choice == "Y":
            print("Great! Keep playing and see how much more you can achieve!")

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

# === Program Start ===
if __name__ == "__main__":
    print("🏰 Welcome to QUEST SHOP [VERSION 1.20.3]")
    state = new_game()
    main()
