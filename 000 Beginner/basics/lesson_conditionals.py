"""Helpful Conditionals

Focus: Write if/elif/else chains for guidance and validation."""
def weather_helper(temp_c):
    if temp_c > 30:
        return("Wear a T-shirt!")
    elif temp_c < 20:
        return("Wear a jacket!")
    else: 
        return("Wear a jumper bro.")

def exercise_1():
    """**Weather Helper**: Write a function `weather_helper(temp_c)` that takes a temperature in Celsius (e.g., `15`) and returns a string suggesting what to wear. Use an if/elif/else chain to handle different temperature ranges."""
    # TODO: Create a weather_helper(temp_c) that returns what to wear.
    temp = 34
    print(f"temp {temp}C -> {weather_helper(temp)}")
    pass


def exercise_2(score):
    """**Grade Validator**: Extend the grading logic to reject scores less than `0` or over `100`. If the score is invalid, print an error message. Otherwise, print the grade."""
    # TODO: Extend grade logic to reject scores less than 0 or over 100 before grading.
    input() = score
    if score > 100 or < 0:
        print("Invalid score")
    else: 
        if score >= 90:
                grade = "A"
        elif score >= 80:
                grade = "B"
        elif score >= 70:
                grade = "C"
        elif score >= 60:
                grade = "D"
        else:
                grade = "F"
    print(f"Score {score} -> Grade {grade}")
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    exercise_2()
    pass

if __name__ == '__main__':
    main()
