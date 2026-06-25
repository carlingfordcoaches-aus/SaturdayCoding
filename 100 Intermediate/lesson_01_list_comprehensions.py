"""List Comprehensions

Focus: Transform sequences with list comprehensions."""


def exercise_1():
    """**Loop vs. Comprehension**: Create a list of squares for numbers 1-5 using a list comprehension. Then, create an equivalent list using a for-loop and compare the readability."""
    # TODO: Replace the list comprehension with an equivalent for-loop and compare readability.
    x = [(i + 1)** 2 for i in range(5)]
    print(x)
    pass

def exercise_2():
    """**Dictionary Comprehension**: Build a dictionary comprehension that maps numbers 1-5 to their cubes."""
    # TODO: Build a dictionary comprehension that maps numbers 1-5 to their cubes.'
    x = {(i + 1)**3 for i in range(5) }
    print(x) 
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
