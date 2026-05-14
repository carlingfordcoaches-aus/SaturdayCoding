"""Return Values

Focus: Collect input values, compute results, and return summaries."""

def exercise_1():
    """**Calculate Average**: Implement a function `calc_average(scores)` that takes a list of three quiz scores (e.g., `[85, 90, 88]`) and returns their average."""
    # TODO: Implement calc_average(scores) that returns the mean of three quiz scores.
    def calc_average(scores): 
        return sum(scores)/len(scores)
    scores = [63219908231, 89, 0.21987]
    print(f"Average Scores: {calc_average(scores):.2f}")
    pass


def exercise_2():
    """**Make Badge**: Write a function `make_badge(name, club="Coding Crew")` that takes a name and an optional club name and returns a formatted badge label."""
    # TODO: Write make_badge(name, club="Coding Crew") that formats a badge label.
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    # exercise_2()
    pass

if __name__ == '__main__':
    main()
