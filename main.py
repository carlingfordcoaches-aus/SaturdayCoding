"""
Space Station Commander
Student Project Template
Follow the Week 1 → Week 10 sections and complete the TODO tasks.
"""

import random
import json


# =====================================================
# WEEK 2 — GAME STATE
# Create and manage the main game data
# =====================================================

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


# =====================================================
# WEEK 3 — MISSION SYSTEM
# Send missions to collect resources
# =====================================================

def send_mission():

    print("\nSending mission...")

    # TODO Week 3:
    # Use random.choice() to select an outcome
    # Possible outcomes: metal, fuel, crystals, nothing

    outcome = None

    # TODO Week 3:
    # If outcome is metal → add random metal
    # If outcome is fuel → add random fuel
    # If outcome is crystals → add random crystals
    # If nothing → print message


# =====================================================
# WEEK 4 — TRADING SYSTEM
# Buy items from a space trader
# =====================================================

shop = {
    "fuel": 10,
    "repair_kit": 15,
    "sensor": 25
}

def trade_menu():

    print("\n--- SPACE TRADER ---")

    # TODO Week 4:
    # Print shop items using a loop

    choice = input("What do you want to buy? ")

    # TODO Week 4:
    # Check if item exists
    # Check if player has enough credits
    # Subtract credits if purchase successful


# =====================================================
# WEEK 5 — RANDOM EVENTS
# Events happen at the end of the day
# =====================================================

def trigger_event():

    # TODO Week 5:
    # Use random.choice() to pick an event
    # Possible events:
    # solar_flare
    # supply_drop
    # nothing

    event = None

    # TODO Week 5:
    # Solar flare → lose energy
    # Supply drop → gain metal
    # Nothing → print message


# =====================================================
# WEEK 7 — CRAFTING / UPGRADES
# Combine or upgrade station systems
# =====================================================

def upgrade_station():

    print("\nStation upgrades coming soon...")

    # TODO Week 7:
    # Create upgrades such as
    # solar panels
    # mining drones
    # defense systems


# =====================================================
# WEEK 6 — SAVE / LOAD SYSTEM
# Save game progress using JSON
# =====================================================

def save_game():

    # TODO Week 6:
    # Save state dictionary to savegame.json

    print("Game saved.")


def load_game():

    global state

    # TODO Week 6:
    # Load the savegame.json file

    print("Game loaded.")


# =====================================================
# WEEK 2 — DAY SYSTEM
# Progress the game each day
# =====================================================

def end_day():

    print("\nEnding day...")

    # TODO Week 2:
    # Increase the day counter

    # TODO Week 2:
    # Reduce energy slightly

    # TODO Week 5:
    # Trigger random event

    print("A new day begins.")


# =====================================================
# WEEK 8 — STATUS DISPLAY / REFACTOR
# Show player information
# =====================================================

def show_status():

    print("\n--- SPACE STATION STATUS ---")

    # TODO Week 8:
    # Print:
    # Day
    # Energy
    # Credits
    # Crew
    # Resources

    print("----------------------------\n")


# =====================================================
# WEEK 1 — MAIN MENU
# Create menu system and user input
# =====================================================

def main_menu():

    print("\n🚀 SPACE STATION COMMANDER")
    print("[1] Send Exploration Mission")
    print("[2] Trade with Space Trader")
    print("[3] Check Station Status")
    print("[4] End Day")
    print("[5] Upgrade Station")
    print("[S] Save Game")
    print("[L] Load Game")
    print("[Q] Quit")


# =====================================================
# WEEK 9 — WIN / LOSE CONDITIONS
# =====================================================

def check_game_status():

    # TODO Week 9:
    # Win if credits >= 500
    # Lose if energy <= 0

    pass


# =====================================================
# WEEK 1 — GAME LOOP
# =====================================================

running = True

while running:

    main_menu()

    choice = input("Choose an option: ").lower()

    if choice == "1":
        send_mission()

    elif choice == "2":
        trade_menu()

    elif choice == "3":
        show_status()

    elif choice == "4":
        end_day()

    elif choice == "5":
        upgrade_station()

    elif choice == "s":
        save_game()

    elif choice == "l":
        load_game()

    elif choice == "q":
        running = False

    else:
        print("Invalid choice.")

    check_game_status()


# =====================================================
# WEEK 10 — POLISHING
# Add help menu, comments, improvements
# =====================================================

print("Game exited.")
