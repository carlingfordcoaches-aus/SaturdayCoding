"""Helpful Conditionals

Focus: Write if/elif/else chains for guidance and validation."""

def exercise_1():
    """**Weather Helper**: Write a function `weather_helper(temp_c)` that takes a temperature in Celsius (e.g., `15`) and returns a string suggesting what to wear. Use an if/elif/else chain to handle different temperature ranges."""\
    
    usertemp = int(input("what's the tempature rn? "))
    if(usertemp<15):
        print("it's best to were your winter clothes: a thick jumper and hoddie or sweater and some long pants or somthing along those lines")
    elif(usertemp>15>25):
        


    # TODO: Create a weather_helper(temp_c) that returns what to wear.
    #pass
  

def exercise_2():
    """**Grade Validator**: Extend the grading logic to reject scores less than `0` or over `100`. If the score is invalid, print an error message. Otherwise, print the grade."""
    # TODO: Extend grade logic to reject scores less than 0 or over 100 before grading.
    pass


def main():
    """Uncomment the exercises you want to run."""
    exercise_1()
    # exercise_2()
    pass

if __name__ == '__main__':
    main()
