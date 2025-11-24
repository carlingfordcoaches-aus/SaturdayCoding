"""Decorators

Focus: Wrap functions to add logging."""


def exercise_1():
    """**Execution Time Decorator**: Extend the `log_call` decorator to measure and print the execution time of the wrapped function using `time.perf_counter`."""
    # TODO: Extend log_call to measure execution time using time.perf_counter.
    pass


def exercise_2():
    """**Caching Decorator**: Write a second decorator that caches the result of a pure function (a function that always returns the same output for the same input). Compose it with the `log_call` decorator."""
    # TODO: Write a second decorator that caches the result of a pure function and compose it with log_call.
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    # exercise_2()
    pass

if __name__ == '__main__':
    main()
