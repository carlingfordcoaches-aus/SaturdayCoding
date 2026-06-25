"""For-Loop Patterns

Focus: Use for-loops with ranges and lists to repeat work."""

def exercise_1():
    """**Multiplication Table**: Use a for-loop with `range()` to print a multiplication table for the number `5`, from 1 to 10."""
    # TODO: Print a multiplication table for numbers 1 through 5.
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")


def exercise_2():
    """**Numbered Chores**: Create a list of chores (e.g., `["Feed the fish", "Clean room", "Take out trash"]`). Use a for-loop with `enumerate()` to print each task with its corresponding number."""
    # TODO: Iterate over a chores list and number each task using enumerate.
    chores = ["Feed the fish", "Clean room", "Take out the trash"]
    for number, chores in enumerate(chores, start=1):
        print(f"{number}. {chores}")
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
