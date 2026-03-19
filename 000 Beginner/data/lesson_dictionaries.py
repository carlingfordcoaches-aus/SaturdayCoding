"""Dictionary Dashboards

Focus: Map keys to values for tracking student progress."""

def exercise_1():
    """**Module Completion**: Create a nested dictionary to track module completion percentages. The outer keys should be module names (e.g., `"loops"`, `"functions"`) and the inner values should be the completion percentage."""
    # TODO: Create a nested dictionary of modules -> completion percent.
    completion = {
        "loops": "40%",
        "functions": "60%"
    }
    for module, percentage in completion.items():
        print(f"{module}:{percentage}")

    pass


def exercise_2():
    """**Describe Student**: Write a function `describe_student(data)` that takes a dictionary of student data (e.g., `{"name": "Skyler", "level": "beginner", "modules": 3}`) and returns a formatted string."""
    # TODO: Write describe_student(data) that returns "Name (level) - N modules".
    def describe_student(data):
        {"name": "Skyler", "level": "beginner", "modules": "3"}
    return
    pass
def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
