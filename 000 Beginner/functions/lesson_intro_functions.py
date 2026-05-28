"""Function Greetings

Focus: Define and call simple functions that format strings."""

def exercise_1():
    """**Student Greeting**: Write a function `greet_student(name, goal)` that takes a student's name (e.g., `"Skyler"`) and their goal (e.g., `"mastering loops"`) and returns a motivational string."""
    # TODO: Write greet_student(name, goal) that returns a motivational string.
    pass
    def greet_student(name, goal, grade_level = None):
        if grade_level:
            return f"Hello {name}(Grade{grade_level})! Keep working towards our goal!"
        else: 
            return f"Hello {name}! Keep working towards {goal}!"
    print(greet_student("Jethro", "Mastering Python",))

def exercise_2():
    """**Optional Grade Level**: Add an optional `grade_level` parameter to the `greet_student` function with a default value of `None`. If a grade level is provided (e.g., `7`), include it in the output."""
    # TODO: Add an optional grade_level parameter with a default value and show how it changes the output.
    pass
def greet_student(name, goal, grade_level = None):
        if grade_level:
            return f"Hello {name}(Grade{grade_level})! Keep working towards our goal!"
        else: 
            return f"Hello {name}! Keep working towards {goal} {grade_level}!"
def grade_level:
    print(greet_student("Jethro", "Mastering Python",))


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
