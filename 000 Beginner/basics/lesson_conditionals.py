"""Helpful Conditionals

Focus: Write if/elif/else chains for guidance and validation."""

def exercise_1():
    """**Weather Helper**: Write a function `weather_helper(temp_c)` that takes a temperature in Celsius (e.g., `15`) and returns a string suggesting what to wear. Use an if/elif/else chain to handle different temperature ranges."""
    # TODO: Create a weather_helper(temp_c) that returns what to wear.
    pass
Temp = float(input(''' what temp is it.
1) 0.01 - 10
2) 11 - 30 
3) 30 - 40
4) 40<                                                     
    '''))
if Temp == 1 :
    print('Wear 5 jackets, 4 jumpers, 4 pants and heater is turned on all the way up')
elif Temp == 2 :
    print('where 1 jacket or jumper and one pair of pants ')
elif Temp == 3 :
    print('eat ice cream and ice blocks, turn on ac, wear shorts')
elif Temp == 4: 
    print('wear shorts and a shirt, ac to the max, dont go outside')
else:
    print('not viable')
def exercise_2():
    """**Grade Validator**: Extend the grading logic to reject scores less than `0` or over `100`. If the score is invalid, print an error message. Otherwise, print the grade."""
    # TODO: Extend grade logic to reject scores less than 0 or over 100 before grading.
    pass
grade = int(input('what score out of 100 did you get:'))

if grade >= 101 :
    print('NOT VIABLE')
elif grade >= 81 :
    print('you got an A')
elif grade >= 61 :
    print('you got a B')
elif grade >= 41 :
    print('you got a C')
elif grade >= 21 :
    print('you got a D')
elif grade >= 0  :                                                         
    print('you got an E')
def main():
    # Uncomment the exercises you want 
      exercise_1
      exercise_2               