"""Error Handling

Focus: Use try/except/else/finally blocks."""


def exercise_1():
    """**Raise ValueError**: In the `safe_divide` function, raise a `ValueError` if non-numeric arguments are provided."""
    # TODO: Raise a ValueError inside safe_divide when non-numeric arguments are provided.
def safe_divide(a, b):
    # Check for non-numeric inputs
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numeric (int or float).")
    
    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    return a / b
    
    pass


def exercise_2():
    """**Logging Context Manager**: Write a context manager that logs "Division starting" before the division and "Division finished" after. Use it with a try/except block to handle potential errors."""
    # TODO: Write a context manager that logs when division starts/ends and pair it with try/except.
    class DivisionLogger:
        def __enter__(self):
            print("🔹 Division operation started.")
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type:
                print(f"⚠️ An error occurred: {exc_value}")
            print("🔹 Division operation ended.")
            return False  
    try:
        with DivisionLogger():
            numerator = 10
            denominator = 0  # Change to non-zero to avoid error
            result = numerator / denominator
            print(f"✅ Result: {result}")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    pass


def main():
    """Uncomment the exercises you want to run."""
    # exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
