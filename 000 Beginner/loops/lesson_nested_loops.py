"""Nested Loop Grids

Focus: Layer loops to build grids or tables."""

def exercise_1():
    """**Tic-Tac-Toe Board**: Use nested for-loops to print the coordinates for a 3x3 tic-tac-toe board."""
    # TODO: Print coordinates for a 3x3 tic-tac-toe board.
    for row in range(3):
        for col in range(3):
            print(f"({row}, {col})", end=" ")
        print() 
    pass


def exercise_2():
    """**Multiplication Grid**: Use nested for-loops to create a 3x3 multiplication grid. Store the results in a list of lists and print each row."""
    # TODO: Store multiplication results in a list of lists and display them nicely.
    
grid = []

for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    grid.append(row)

for row in grid:
    print(f"{row[0]}  {row[1]}  {row[2]}")
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    # exercise_2()
    pass

if __name__ == '__main__':
    main()
