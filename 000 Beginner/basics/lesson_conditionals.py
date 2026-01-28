"""Helpful Conditionals

Focus: Write if/elif/else chains for guidance and validation."""
def weather_helper(temp_c):
    if temp_c > 25:
        return "Wear a Shirt"
    elif temp_c < 15:
        return "Wear a Sweater"
    else:
        return "Wear a Jacket"

def exercise_1():
    """**Weather Helper**: Write a function `weather_helper(temp_c)` that takes a temperature in Celsius (e.g., `15`) and returns a string suggesting what to wear. Use an if/elif/else chain to handle different temperature ranges."""
    # TODO: Create a weather_helper(temp_c) that returns what to wear.
temp = 28
print(f"Temp {temp}C -> {weather_helper(temp)}")


pass

def exercise_2():
    """**Grade Validator**: Extend the grading logic to reject scores less than `0` or over `100`. If the score is invalid, print an error message. Otherwise, print the grade."""
    # TODO: Extend grade logic to reject scores less than 0 or over 100 before grading.
    pass
score = 90
if grade < 85
   return "A"

elif grade > 85
   return "B"

elif grade > 70
   return "C"

elif grade > 50
   return "D"

elif grade > 25
   return "E"

def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    # exercise_2()
    pass

if __name__ == '__main__':
    main()
