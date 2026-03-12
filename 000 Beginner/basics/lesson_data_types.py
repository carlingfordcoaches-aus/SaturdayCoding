"""Data Type Detective

Focus: Recognize Python data types and convert between them."""

def exercise_1():
    """**Build a Mixed-Type List**: Create a list containing the following items: `42` (int), `"projects"` (str), `3.14` (float), and `True` (bool). Iterate through the list and print each value along with its data type."""
    # TODO: Build a list containing an int, float, string, and bool, then print each value with its type.
    mixed_list = 42, "projects", 3.14, True
    for item in mixed_list: 
        print(f"Value {item} -> {type(item)}")
    pass


def exercise_2():
    """**Combine Different Types**: Create a numeric string `"10"` and a float `45.5`. Convert the string to an integer and add it to the float. Print the total."""
    # TODO: Turn a numeric string into an int and add it to a float to show the total.
    numeric_string = "10"
    float_number = 45.5 
    total = int(numeric_string) + float_number
    print(f"Combined total : {total}")
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
