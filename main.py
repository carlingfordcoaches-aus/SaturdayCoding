
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
        "crystals": 0,
        "miningDrones": 0,
        "fusion_reactor":0,
        "defence_systems": 0,
        "solar_pannels": 0
    }
}


# =====================================================
# WEEK 3 — MISSION SYSTEM
# Send missions to collect resources
# =====================================================

def send_mission():

    print("\n♾️ Sending mission...")
    if state["energy"] < 10:
        print ("♾️ Not enough fuel")
    else:
        ed()

def ed():
    state["energy"] -= 10
    outcome = random.randint(1, 5)
    if outcome == 1:
        print("♾️ Mission successful! You found some metal.")
        state["resources"]["metal"] += random.randint(5, 15)
    elif outcome == 2:
        print("♾️ Mission successful! You found some fuel.")
        state["resources"]["fuel"] += random.randint(5, 15)
    elif outcome == 3:
        print("♾️ Mission successful! You found some crystals.")
        state["resources"]["crystals"] += random.randint(5, 15)
    elif outcome == 4:
        print("♾️ Aliens raided your ship, you lost some recources!")
        state["resources"]["metal"] = max(0, state["resources"]["metal"] - random.randint(1, 5))
        state["resources"]["fuel"] = max(0, state["resources"]["fuel"] - random.randint(1, 5))
        state["resources"]["crystals"] = max(0, state["resources"]["crystals"] - random.randint(1, 5))
    else:
        print("♾️ Mission failed. No resources found.")
    
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

    print("\n--- ♾️ SPACE TRADER ♾️ ---")
    print("♾️ You have {} credits.".format(state["credits"]))
    print("♾️ [1] Buy fuel (10 credits)")
    print("♾️ [2] Buy repair kit (15 credits)")
    print("♾️ [3] Buy sensor (25 credits)")
    print("♾️ [4] Sell metal (5 credits each)")
    print("♾️ [5] Trade fuel (+1 energy each)")
    print("♾️ [0] Back")

    # TODO Week 4:
    # Print shop items using a loop

    choice = input("> ")
    if choice == "1":
        print("♾️ You bought fuel.")
        state["credits"] -= shop["fuel"]
        state["resources"]["fuel"] += 10
    elif choice == "2":
        print("♾️ You bought a repair kit.")
        state["credits"] -= shop["repair_kit"]
        state["resources"]["repair_kit"] += 1
    elif choice == "3":
        print("♾️ You bought a sensor.")
        state["credits"] -= shop["sensor"]
        state["resources"]["sensor"] += 1
    elif choice == "4":
        print("♾️ How many do you want to sell?")
        quantity = int(input("> "))
        if quantity <= state["resources"]["metal"]:
            state["credits"] += quantity * 5
            state["resources"]["metal"] -= quantity
            print(f"♾️ You sold {quantity} metal.")
        else:
            print("♾️ Not enough metal to sell.")
    elif choice == "5":
        print("♾️ How many fuel do you want to trade?")
        quantity = int(input("> "))
        if quantity <= state["resources"]["fuel"]:
            state["energy"] += quantity
            state["resources"]["fuel"] -= quantity
            print(f"♾️ You traded {quantity} fuel for {quantity} energy.")
        else:
            print("♾️ Not enough fuel to trade.")
    elif choice == "0":
        print("♾️ You left the space trader.")
    else:
        print("♾️ Invalid choice.")
    

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

    print("\n--- ♾️ Station Upgrades ♾️ ---")
    print("♾️ [1] Solar Panels (20 credits) - Increases energy recovery")
    print("♾️ [2] Energy Pack (30 credits) - Increases energy by 50")
    print("♾️ [3] Defense Systems (40 credits) - Reduces negative event impact")
    print("♾️ [4] Fusion Reactor (50 credits) - Increases max energy")
    print("♾️ [5] Mining Drones (50 crystals) - Increases mining efficiency")
    print("♾️ [0] Back")

    thing = int(input(">"))
    if thing == 1:
        e()
    elif thing == 2:
        d()
    elif thing == 3:
        c()
    elif thing == 4:
        b()
    elif thing == 5:
        a()
    elif thing == 0:
        print("♾️ You left the upgrade menu.")
    else:
        print("♾️ Invalid input. Please try again.")
        upgrade_station()

def a():
    if state["recources"]["crystals"] >= 50:
        print("♾️ You bought a mining drone")
        state["recources"]["miningDrones"] += 1
        state["recources"]["crystals"] -= 50
    else:
        print("♾️ You don't have enough recources")

def b():
    if state["credits"] >= 50:
        print("♾️ You bought a fusion reactor.")
        state["credits"] -= 50
        state["recources"]["fusion_reactor"] += 1
    else:
        print("♾️ You don't have enough recources")
    
def c():
    if state["credits"] >= 40:
        print("♾️ You bought defence systems.")
        state["credits"] -= 40
        state["resources"]["defense_systems"] += 1
    else:
        print("♾️ You don't have enough recources")

def d():
    if state["credits"] >= 30:
        print("♾️ Energy Pack")
        state["credits"] -= 30
        state["energy"] += 50
    else:
        print("♾️ You don't have enough recources")

def e():
    if state["credits"] >= 20:
        print("♾️ You bought solar pannels")
        state["credits"] -= 20
        state["resources"]["solar_pannels"] += 1
    else:
        print("♾️ You don't have enough recources")
    # TODO Week 7:
    # Create upgrades such as
    # solar panels
    # mining drones
    # defense systems
    # fusion reactor

# =====================================================
# WEEK 6 — SAVE / LOAD SYSTEM
# Save game progress using JSON
# =====================================================
def attack_aliens():
    if state["resources"]["defense_systems"] == 0:
        print("♾️ Your station doesn't have defense systems")
    elif state["resources"]["defense_systems"] == 1:
        print("♾️ Your station has 1 defense system, you can defend against small alien attacks but not large ones.")
        print("♾️ You gained 10 credits from defending against the small alien attack but your defense mechanisms were damaged and you lost 1 defense system.")
        state["credits"] += 10
        state["resources"]["defense_systems"] -= 1
    elif state["resources"]["defense_systems"] == 2:
        print("♾️ Your station has 2 defense systems, you can defend against small and large alien attacks.")
        print("♾️ You gained 20 credits from defending against the large alien attack but your defense mechanisms were damaged and you lost 1 defense system.")
        state["credits"] += 20
        state["resources"]["defense_systems"] -= 1
    elif state["resources"]["defense_systems"] == 3:
        print("♾️ Your station has 3 defense systems, you can defend against small and large alien attacks.")
        print("♾️ You gained 30 credits from defending against the large alien attack and your defense systems were not damaged.")
        state["credits"] += 30
    elif state["resources"]["defense_systems"] == 4:
        print("♾️ Your station has {} defense systems, you can defend against small and large alien attacks.".format(state["resources"]["defense_systems"]))
        print("♾️ You gained 30 credits from defending against the large alien attack and your defense systems were not damaged.")
        state["credits"] += 30
    elif state["resources"]["defense_systems"] >= 5:
        print("♾️ Your station destroyed all alien ships and gained 50 credits but your defense systems were damaged and you lost 3 defense system.")
        state["credits"] += 50
        state["resources"]["defense_systems"] -= 3
    else:
        print("♾️ Invalid number of defense systems.")

def save_game():
    try:
        with open('main_save.json', 'w') as f:
            json.dump(state, f, indent=2)
        print("✅ Game saved successfully.♾️ ")
    except Exception as e:
        print(f"⚠️ Error saving game: {e}")



def load_game():
    try:
        with open('main_save.json', 'r') as f:
            data = json.load(f)
        print("✅ Game loaded successfully.♾️")
        return data
    except FileNotFoundError:
        print("⚠️ No save file found.♾️ ")
        return None
    except Exception as e:
        print(f"⚠️ Error loading game: {e}")
        return None

    # TODO Week 6:
    # Load the savegame.json file

    print("♾️ Game loaded.")


# =====================================================
# WEEK 2 — DAY SYSTEM
# Progress the game each day
# =====================================================

def end_day():

    print("\n♾️ Ending day...")
    state["day"] += 1
    state["energy"] = min(100, state["energy"] + 20)
    state["resources"]["fuel"] -= 5
    print("♾️ Your station consumed 5 fuel for the day.")
    print("♾️ It is now day {}.".format(state["day"]))
    if state["resources"]["fuel"] <= 0:
        print("♾️ You ran out of fuel and your station is now uninhabitable.")
        print("---GAME OVER---")
        raise SystemExit(0)
    


    # TODO Week 2:
    # Increase the day counter

    # TODO Week 2:
    # Reduce energy slightly

    # TODO Week 5:
    # Trigger random event




# =====================================================
# WEEK 8 — STATUS DISPLAY / REFACTOR
# Show player information
# =====================================================

def show_status():

    print("\n--- ♾️ SPACE STATION STATUS ♾️ ---")

    print("♾️ Day: {} | Energy: {} | Credits: {} | Crew: {} ".format(state["day"], state["energy"], state["credits"], state["crew"]))
    print(" Recources + Upgrades: {}".format(state["resources"]))
    # TODO Week 8:
    # Print:
    # Day
    # Energy
    # Credits
    # Crew
    # Resources

    print("♾️ ---------------------------- ♾️\n")


# =====================================================
# WEEK 1 — MAIN MENU
# Create menu system and user input
# =====================================================

def main_menu():

    print("\n--- ♾️ SPACE STATION COMMANDER ♾️ ---")
    print("♾️ ------------------------------ ♾️")
    print("♾️  Day {} | Energy: {} | Credits: {} | Crew: {} ".format(state["day"], state["energy"], state["credits"], state["crew"]))
    print("♾️ [1] Send Exploration Mission")
    print("♾️ [2] Trade with Space Trader")
    print("♾️ [3] Check Station Status")
    print("♾️ [4] End Day")     
    print("♾️ [5] Upgrade Station")
    print("♾️ [6] Attack Aliens")
    print("♾️ [S] Save Game")
    print("♾️ [L] Load Game")
    print("♾️ [Q] Quit")


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
        print("♾️ Consider trading fuel for energy or ending the day to recover energy.")

    elif choice == "2":
        trade_menu()

    elif choice == "3":
        show_status()

    elif choice == "4":
        end_day()

    elif choice == "5":
        upgrade_station()
    
    elif choice == "6":
        attack_aliens()

    elif choice == "s":
        save_game()

    elif choice == "l":
        load_game()

    elif choice == "q":
        running = False

    else:
        print("♾️ Invalid choice.")

    check_game_status()


# =====================================================
# WEEK 10 — POLISHING
# Add help menu, comments, improvements
# =====================================================

print("♾️ Game exited.")