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
    outcome = random.randint(1, 5)
    if outcome == 1:
        print("Mission successful! You found some metal.")
        state["resources"]["metal"] += random.randint(5, 15)
    elif outcome == 2:
        print("Mission successful! You found some fuel.")
        state["resources"]["fuel"] += random.randint(5, 15)
    elif outcome == 3:
        print("Mission successful! You found some crystals.")
        state["resources"]["crystals"] += random.randint(5, 15)
    elif outcome == 4:
        print("Aliens raided your ship, you lost some recources!")
        state["resources"]["metal"] = max(0, state["resources"]["metal"] - random.randint(1, 5))
        state["resources"]["fuel"] = max(0, state["resources"]["fuel"] - random.randint(1, 5))
        state["resources"]["crystals"] = max(0, state["resources"]["crystals"] - random.randint(1, 5))
    else:
        print("Mission failed. No resources found.")
    
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
    print("You have {} credits.".format(state["credits"]))
    print("[1] Buy fuel (10 credits)")
    print("[2] Buy repair kit (15 credits)")
    print("[3] Buy sensor (25 credits)")
    print("[4] Sell metal (5 credits each)")
    print("[5] Trade fuel (+1 energy each)")
    print("[0] Back")

    # TODO Week 4:
    # Print shop items using a loop

    choice = input("> ")
    if choice == "1":
        print("You bought fuel.")
        state["credits"] -= shop["fuel"]
        state["resources"]["fuel"] += 10
    elif choice == "2":
        print("You bought a repair kit.")
        state["credits"] -= shop["repair_kit"]
        state["resources"]["repair_kit"] += 1
    elif choice == "3":
        print("You bought a sensor.")
        state["credits"] -= shop["sensor"]
        state["resources"]["sensor"] += 1
    elif choice == "4":
        print("How many do you want to sell?")
        quantity = int(input("> "))
        if quantity <= state["resources"]["metal"]:
            state["credits"] += quantity * 5
            state["resources"]["metal"] -= quantity
            print(f"You sold {quantity} metal.")
        else:
            print("Not enough metal to sell.")
    elif choice == "5":
        print("How many fuel do you want to trade?")
        quantity = int(input("> "))
        if quantity <= state["resources"]["fuel"]:
            state["energy"] += quantity
            state["resources"]["fuel"] -= quantity
            print(f"You traded {quantity} fuel for {quantity} energy.")
        else:
            print("Not enough fuel to trade.")
    elif choice == "0":
        print("You left the space trader.")
    else:
        print("Invalid choice.")

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
    print(" Day: {} | Energy: {} | Credits: {} | Crew: {} | Recources: {}".format(state["day"], state["energy"], state["credits"], state["crew"], state["resources"]))
    # TODO Week 8:
    # Print:
    # Day
    # Energy
    # Credits
    # Crew
    # Resources

    print("----------------------------\n")


def main_menu():

    print("\n🚀 SPACE STATION COMMANDER")
    print("------------------------------")
    print(" Day {} | Energy: {} | Credits: {} | Crew: {} | Resources: {}".format(state["day"], state["energy"], state["credits"]))
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

    choice = input("> ").lower()

    if choice == "1":
        send_mission()
        state["energy"] -= 10
        if state["energy"] <= 10:
            print("Not enough energy for exploration mission.")
            print("Consider trading fuel for energy or ending the day to recover energy.")

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
