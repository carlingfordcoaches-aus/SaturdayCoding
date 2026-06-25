"""While-Loop Control

Focus: Build while-loops with sentinels and counters."""

def exercise_1():
    """**Command Prompt**: Write a while-loop that repeatedly prompts the user for a command until they type `"exit"`."""
    # TODO: Prompt for commands until the user types "exit".
    while True:
        command = input("Enter a command: ")
    
        if command.strip().lower() == "exit":
            print("Exiting...")
        if command.strip().lower() == "start":
            print("Starting...")
        if command.strip().lower() == "pause":
            print("Pausing...")
        break
    pass


def exercise_2():
    """**Countdown Timer**: Create a while-loop that counts down from `3` to `1` and then prints `"Time!"`."""
    # TODO: Create a countdown timer that prints "Time!" at the end.
    countdown = 74

    while countdown > 0:
            print(countdown)
    countdown -= 1
    print("Time!")
        
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
