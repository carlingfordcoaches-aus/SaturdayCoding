# Python Lesson Roadmap

This repository is organized into three learning tracks (beginner, intermediate, advanced). Run each lesson file to see a guided demo, then complete the matching exercises below. Ask your coach for any hints or help!

## Beginner Track

Beginner lessons now live in themed folders (basics, loops, functions, data, input). Work through each topic in order to build confidence before moving to the intermediate track.

### Basics
Foundational skills for working with numbers, types, and comparisons.

#### Variables & Numbers (`beginner/basics/lesson_variables_numbers.py`)
- **Focus**: Manage integers and floats to track classroom progress.
- **Exercises**:
  1. **Track Progress**: Create two variables, `completed_lessons` (int) and `total_lessons` (int). Assign them values `3` and `10` respectively. Calculate the percentage of completed lessons and print a progress bar.
  2. **Convert Minutes to Hours**: Create a variable `study_minutes` and assign it the value `90`. Convert the minutes to hours and print the result in a formatted sentence.
- **Example Output**:
  ```text
  Progress: 3/10 lessons (30.0%)
  Study time: 90 minutes = 1.5 hours
  ```

#### Data Type Detective (`beginner/basics/lesson_data_types.py`)
- **Focus**: Recognize Python data types and convert between them.
- **Exercises**:
  1. **Build a Mixed-Type List**: Create a list containing the following items: `42` (int), `"projects"` (str), `3.14` (float), and `True` (bool). Iterate through the list and print each value along with its data type.
  2. **Combine Different Types**: Create a numeric string `"10"` and a float `45.5`. Convert the string to an integer and add it to the float. Print the total.
- **Example Output**:
  ```text
  Value 42 -> <class 'int'>
  Value 'projects' -> <class 'str'>
  Value 3.14 -> <class 'float'>
  Value True -> <class 'bool'>
  Combined total: 55.5
  ```

#### Helpful Conditionals (`beginner/basics/lesson_conditionals.py`)
- **Focus**: Write if/elif/else chains for guidance and validation.
- **Exercises**:
  1. **Weather Helper**: Write a function `weather_helper(temp_c)` that takes a temperature in Celsius (e.g., `15`) and returns a string suggesting what to wear. Use an if/elif/else chain to handle different temperature ranges.
  2. **Grade Validator**: Extend the grading logic to reject scores less than `0` or over `100`. If the score is invalid, print an error message. Otherwise, print the grade.
- **Example Output**:
  ```text
  Temp 15°C -> Wear a sweater.
  Score 105 -> Invalid input.
  ```


### Loops Lab
Practice looping patterns with ranges, lists, and nested grids.

#### For-Loop Patterns (`beginner/loops/lesson_for_loops.py`)
- **Focus**: Use for-loops with ranges and lists to repeat work.
- **Exercises**:
  1. **Multiplication Table**: Use a for-loop with `range()` to print a multiplication table for the number `5`, from 1 to 10.
  2. **Numbered Chores**: Create a list of chores (e.g., `["Feed the fish", "Clean room", "Take out trash"]`). Use a for-loop with `enumerate()` to print each task with its corresponding number.
- **Example Output**:
  ```text
  1 x 5 = 5
  2 x 5 = 10
  ...
  10 x 5 = 50
  Task 1: Feed the fish
  Task 2: Clean room
  Task 3: Take out trash
  ```

#### While-Loop Control (`beginner/loops/lesson_while_loops.py`)
- **Focus**: Build while-loops with sentinels and counters.
- **Exercises**:
  1. **Command Prompt**: Write a while-loop that repeatedly prompts the user for a command until they type `"exit"`.
  2. **Countdown Timer**: Create a while-loop that counts down from `3` to `1` and then prints `"Time!"`.
- **Example Output**:
  ```text
  Command> practice
  Command> study
  Command> exit
  Countdown: 3 2 1 Time!
  ```

#### Nested Loop Grids (`beginner/loops/lesson_nested_loops.py`)
- **Focus**: Layer loops to build grids or tables.
- **Exercises**:
  1. **Tic-Tac-Toe Board**: Use nested for-loops to print the coordinates for a 3x3 tic-tac-toe board.
  2. **Multiplication Grid**: Use nested for-loops to create a 3x3 multiplication grid. Store the results in a list of lists and print each row.
- **Example Output**:
  ```text
  (row 1, col 1)
  (row 1, col 2)
  (row 1, col 3)
  (row 2, col 1)
  ...
  (row 3, col 3)
  Grid row: [1, 2, 3]
  Grid row: [2, 4, 6]
  Grid row: [3, 6, 9]
  ```


### Function Workshop
Create reusable helpers with parameters, return values, and docstrings.

#### Function Greetings (`beginner/functions/lesson_intro_functions.py`)
- **Focus**: Define and call simple functions that format strings.
- **Exercises**:
  1. **Student Greeting**: Write a function `greet_student(name, goal)` that takes a student's name (e.g., `"Skyler"`) and their goal (e.g., `"mastering loops"`) and returns a motivational string.
  2. **Optional Grade Level**: Add an optional `grade_level` parameter to the `greet_student` function with a default value of `None`. If a grade level is provided (e.g., `7`), include it in the output.
- **Example Output**:
  ```text
  Hello Skyler! Keep working toward mastering loops.
  Hello Skyler (Grade 7)! Keep working toward mastering loops.
  ```

#### Return Values (`beginner/functions/lesson_parameters_returns.py`)
- **Focus**: Collect input values, compute results, and return summaries.
- **Exercises**:
  1. **Calculate Average**: Implement a function `calc_average(scores)` that takes a list of three quiz scores (e.g., `[85, 90, 88]`) and returns their average.
  2. **Make Badge**: Write a function `make_badge(name, club="Coding Crew")` that takes a name and an optional club name and returns a formatted badge label.
- **Example Output**:
  ```text
  Average score: 87.67
  Badge -> Skyler | Coding Crew
  ```

#### Docstrings & Imports (`beginner/functions/lesson_docstrings_modules.py`)
- **Focus**: Explain functions with docstrings and reuse standard modules.
- **Exercises**:
  1. **Add Docstrings**: Add docstrings to the `calc_average` and `make_badge` functions from the previous lesson, explaining their parameters and what they return.
  2. **Use Math Module**: Import the `math` module and use it to calculate the area of a circle with a radius of `3`.
- **Example Output**:
  ```text
  Circle area (r=3): 28.27
  ```


### Data Structures
Organize information with lists, dictionaries, sets, and tuples.

#### List Playground (`beginner/data/lesson_lists.py`)
- **Focus**: Slice, append, and summarize lists of lesson data.
- **Exercises**:
  1. **Lesson Durations**: Create a list of lesson durations in hours (e.g., `[0.5, 0.75, 1.0]`). Calculate and print the total number of hours.
  2. **Help-Desk Queue**: Simulate a help-desk queue using a list. Start with a list of names (e.g., `["Alice", "Bob", "Charlie"]`). Use `insert()` to add a new name to the beginning of the queue and `pop()` to remove the last name. Print the queue after each operation.
- **Example Output**:
  ```text
  Durations: [0.5, 0.75, 1.0] -> 2.25h
  Initial queue: ['Alice', 'Bob', 'Charlie']
  Queue after insert: ['David', 'Alice', 'Bob', 'Charlie']
  Queue after pop: ['David', 'Alice', 'Bob']
  ```

#### Dictionary Dashboards (`beginner/data/lesson_dictionaries.py`)
- **Focus**: Map keys to values for tracking student progress.
- **Exercises**:
  1. **Module Completion**: Create a nested dictionary to track module completion percentages. The outer keys should be module names (e.g., `"loops"`, `"functions"`) and the inner values should be the completion percentage.
  2. **Describe Student**: Write a function `describe_student(data)` that takes a dictionary of student data (e.g., `{"name": "Skyler", "level": "beginner", "modules": 3}`) and returns a formatted string.
- **Example Output**:
  ```text
  loops: 60%
  functions: 80%
  Skyler (beginner) - 3 modules
  ```

#### Sets & Tuples (`beginner/data/lesson_sets_tuples.py`)
- **Focus**: Use sets for uniqueness and tuples for ordered pairs.
- **Exercises**:
  1. **Unique Clubs**: Create a list of club names with duplicates (e.g., `["Robotics", "Chess", "Robotics"]`). Use a set to find and print the unique club names.
  2. **Seat Coordinates**: Store classroom seat coordinates as a list of tuples, where each tuple represents a `(row, seat)` pair (e.g., `(1, "A")`, `(1, "B")`). Iterate over the list and print each coordinate.
- **Example Output**:
  ```text
  Unique clubs: {'Robotics', 'Chess'}
  (row=1, seat=A)
  (row=1, seat=B)
  ```


### Input & Files
Format text, gather user input, and read/write simple files.

#### String Stylizer (`beginner/io/lesson_strings.py`)
- **Focus**: Clean user text and combine it with f-strings.
- **Exercises**:
  1. **Title-Cased Greeting**: Take a name with extra whitespace (e.g., `"  aarya  "`) and use string methods to strip the whitespace and print a title-cased greeting.
  2. **Topic Arrows**: Take a comma-separated string of favorite topics (e.g., `"loops,games,art"`) and use string methods to split it into a list and then rejoin the items with arrows.
- **Example Output**:
  ```text
  Welcome, Aarya!
  loops -> games -> art
  ```

#### Friendly File I/O (`beginner/io/lesson_file_io.py`)
- **Focus**: Save notes to disk and read them back with numbering.
- **Exercises**:
  1. **Numbered Notes**: Write three motivational lines to a text file named `notes.txt`. Then, read the file and print each line with a number in front of it.
  2. **Save/Load Functions**: Wrap the save and load actions from the previous exercise in helper functions `save_notes(notes)` and `load_notes()`.
- **Example Output**:
  ```text
  1. Keep practicing.
  2. Test often.
  3. You've got this!
  Loaded notes successfully.
  ```

#### Interactive Quiz (`beginner/io/lesson_user_input.py`)
- **Focus**: Gather input safely and provide instant feedback.
- **Exercises**:
  1. **Math Quiz**: Build a two-question math quiz that asks the user for the answer and scores them.
  2. **Input Validation**: Validate that the user's input is a numeric answer before converting it to an `int` or `float`. If the input is not numeric, prompt the user to enter a valid number.
- **Example Output**:
  ```text
  What is 4 + 3? 7
  Correct!
  What is 10 - 2? 8
  Correct!
  Score: 2/2
  ```

## Intermediate Track

Skills build lesson by lesson start at 01 and keep going. Each entry lists the main idea, follow-up exercises, and a captured snippet of console output so you know what success looks like.

### List Comprehensions (`intermediate/lesson_01_list_comprehensions.py`)
- **Focus**: Transform sequences with list comprehensions.
- **Exercises**:
  1. **Loop vs. Comprehension**: Create a list of squares for numbers 1-5 using a list comprehension. Then, create an equivalent list using a for-loop and compare the readability.
  2. **Dictionary Comprehension**: Build a dictionary comprehension that maps numbers 1-5 to their cubes.
- **Example Output**:
  ```text
  Comprehension: [1, 4, 9, 16, 25]
  Manual loop: [1, 4, 9, 16, 25]
  {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
  ```

### Error Handling (`intermediate/lesson_02_error_handling.py`)
- **Focus**: Use try/except/else/finally blocks.
- **Exercises**:
  1. **Raise ValueError**: In the `safe_divide` function, raise a `ValueError` if non-numeric arguments are provided.
  2. **Logging Context Manager**: Write a context manager that logs "Division starting" before the division and "Division finished" after. Use it with a try/except block to handle potential errors.
- **Example Output**:
  ```text
  Division starting
  Result: 5.0
  Division finished
  ValueError: Non-numeric value provided
  ```

### Generators (`intermediate/lesson_03_generators.py`)
- **Focus**: Build a generator for incremental IDs.
- **Exercises**:
  1. **Generator with Limit**: Add a `limit` parameter to the `id_sequence` generator. When the limit is reached, the generator should raise `StopIteration` with a message.
  2. **Even ID Generator**: Create a generator expression that yields only the even IDs from the `id_sequence` generator.
- **Example Output**:
  ```text
  ID -> 1
  ID -> 2
  Even IDs: [2, 4]
  StopIteration: Limit reached
  ```

### Decorators (`intermediate/lesson_04_decorators.py`)
- **Focus**: Wrap functions to add logging.
- **Exercises**:
  1. **Execution Time Decorator**: Extend the `log_call` decorator to measure and print the execution time of the wrapped function using `time.perf_counter`.
  2. **Caching Decorator**: Write a second decorator that caches the result of a pure function (a function that always returns the same output for the same input). Compose it with the `log_call` decorator.
- **Example Output**:
  ```text
  slow_add took 0.10s
  Result: 5
  slow_add took 0.00s (cache hit)
  ```

### Classes & Objects (`intermediate/lesson_05_classes.py`)
- **Focus**: Use classes to encapsulate behavior.
- **Exercises**:
  1. **Method Chaining**: Add a `level_up` method to the `Lesson` class that upgrades the difficulty and returns `self` to allow for method chaining.
  2. **Subclassing**: Create a `VideoLesson` subclass that inherits from `Lesson` and adds a `runtime_minutes` attribute. Override the `describe` method to include the runtime.
- **Example Output**:
  ```text
  Classes (advanced)
  Decorators (intermediate) - 12 minutes
  ```

### Dataclasses (`intermediate/lesson_06_dataclasses.py`)
- **Focus**: Leverage dataclasses for simple models.
- **Exercises**:
  1. **Computed Property**: Add a computed property to the `Assignment` dataclass that returns a "slugified" version of the title (e.g., `"Loops Drill"` becomes `"loops-drill"`).
  2. **Sorting Dataclasses**: Instantiate several `Assignment` objects and sort them by `max_score` in ascending order using the `sorted()` function and `operator.attrgetter`.
- **Example Output**:
  ```text
  Slug -> loops-drill
  Sorted: [Assignment(title='Loops Drill', max_score=30), Assignment(title='Dataclasses', max_score=50)]
  ```

### Type Hints (`intermediate/lesson_07_type_hints.py`)
- **Focus**: Add static typing hints and TypedDict usage.
- **Exercises**:
  1. **Sequence Annotation**: Annotate the `tag_lesson` function to accept a `Sequence[str]` instead of `List[str]` and explain in a comment why this is a good practice.
  2. **Protocols**: Create a `Protocol` representing a renderer with a `render(title: str) -> str` method. Implement two different classes that adhere to this protocol.
- **Example Output**:
  ```text
  Decorators => functions, wrappers
  *** Type hints ***
  PROTOCOLS ROCK
  ```

### Context Managers (`intermediate/lesson_08_context_managers.py`)
- **Focus**: Create custom context managers.
- **Exercises**:
  1. **Timer Context Manager**: Write a context manager class (not a decorator) that times how long a block of code takes to run.
  2. **File Mode Parameter**: Refactor the `open_lesson` context manager to accept a `mode` parameter (`"w"` for write, `"r"` for read) and test both flows.

### Logging Basics (`intermediate/lesson_09_logging.py`)
- **Focus**: Configure logging for reusable modules.
- **Exercises**:
  1. **File Handler**: Configure a file handler to write logs to a file named `logs/intermediate.log`.
  2. **Structured Logging**: Add structured data (e.g., `lesson_name`, `user`) to the log messages using keyword arguments.

### Testing Primer (`intermediate/lesson_10_testing.py`)
- **Focus**: Show a pytest-style test function.
- **Exercises**:
  1. **Test Module**: Split the `add` function into a new module and import it into the test file to mimic a real project structure.
  2. **Parametrized Tests**: Use `pytest.mark.parametrize` to test the `add` function with positive numbers, negative numbers, and zero.

## Advanced Track

Skills build lesson by lesson start at 01 and keep going. Each entry lists the main idea, follow-up exercises, and a captured snippet of console output so you know what success looks like.

### Study Timer (`advanced/lesson_01_study_timer.py`)
- **Focus**: Build a friendly study timer that breaks sessions into focus and rest blocks.
- **Exercises**:
  1. **User-Defined Timer**: Ask the user how many minutes they want to focus and rest, then run the timer with their choices.
  2. **Encouraging Messages**: Add encouraging messages (e.g., `"Great job!"`, `"Grab some water!"`) that print each time a focus or rest block finishes.
- **Example Output**:
  ```text
  Focus: 30 seconds left
  Focus block complete! Great job!
  Break: 15 seconds left
  ```

### Math Quiz (`advanced/lesson_02_math_quiz.py`)
- **Focus**: Create a mini math quiz game that tracks the score for each player.
- **Exercises**:
  1. **Hints for Close Answers**: Let players answer the quiz questions using `input()`. If their answer is close to the correct answer (e.g., off by 1), give them a hint.
  2. **Leaderboard**: Store each player's score in a dictionary. At the end of the game, display a leaderboard with the players and their scores.
- **Example Output**:
  ```text
  What is 5 + 7? -> 12
  Correct!
  What is 3 + 8? -> 10
  Close, try again!
  Leaderboard:
  Maya: 3
  Alex: 2
  ```

### Flashcard Helper (`advanced/lesson_03_flashcard_app.py`)
- **Focus**: Model a simple flashcard helper using dictionaries and loops.
- **Exercises**:
  1. **Shuffle and Quiz**: Shuffle the flashcards and quiz the player by showing them only the term first.
  2. **Save to File**: Save the flashcards to a text file named `flashcards.txt` so they can be loaded later.
- **Example Output**:
  ```text
  Term: Planet?
  A big ball in space that orbits a star.
  Saved 3 cards to flashcards.txt
  ```

### Budget Tracker (`advanced/lesson_04_budget_tracker.py`)
- **Focus**: Track weekly allowance spending with lists and simple calculations.
- **Exercises**:
  1. **Allowance Warning**: Ask the user for their weekly allowance. As they add expenses, warn them when they have only $5 remaining.
  2. **Sort Purchases**: Sort the purchases from most to least expensive before printing the summary.
- **Example Output**:
  ```text
  Warning! Only $4.75 left.
  Book: $8.00
  Snacks: $3.25
  ```

### Club Roster (`advanced/lesson_05_club_roster.py`)
- **Focus**: Use classes to organize a school club roster.
- **Exercises**:
  1. **Search by Role**: Add a method to the `Club` class that searches for members by their role (e.g., `"Captain"`) and prints their names.
  2. **SportsClub Subclass**: Create a `SportsClub` subclass that inherits from `Club`, tracks the name of the sport, and overrides the `badge_text` method.
- **Example Output**:
  ```text
  Mina - Grade 9 (Captain)
  Leo - Soccer (Player)
  ```

### Weather Report (`advanced/lesson_06_weather_report.py`)
- **Focus**: Summarize weekly weather using dictionaries and helper functions.
- **Exercises**:
  1. **Celsius Conversion**: Convert the temperatures from Fahrenheit to Celsius and show both scales in the summary.
  2. **Daily Report**: Ask the user which day they want a report for and print the high/low temperature pair for that day.
- **Example Output**:
  ```text
  Mon: High 72°F/22.2°C, Low 60°F/15.6°C
  Tue: High 75°F/23.9°C, Low 62°F/16.7°C
  ```

### Schedule Planner (`advanced/lesson_07_schedule_planner.py`)
- **Focus**: Build a day planner that keeps tasks in order.
- **Exercises**:
  1. **Remove Task**: Allow the user to remove a task by typing its time (e.g., `"09:00"`).
  2. **Export to File**: Export the ordered schedule to a file named `my_schedule.txt`.
- **Example Output**:
  ```text
  Removed tasks at 09:00
  Saved schedule to my_schedule.txt
  ```

### Guessing Game (`advanced/lesson_08_guess_game.py`)
- **Focus**: Code a number guessing game with friendly hints.
- **Exercises**:
  1. **User Input**: Replace the hardcoded guesses with `input()` and keep looping until the player guesses the correct number.
  2. **Guess Counter**: Track how many guesses the player uses. If they solve it in three tries or less, celebrate their win.
- **Example Output**:
  ```text
  Too low!
  Too high!
  You got it in 3 guesses!
  ```

### CSV Scoreboard (`advanced/lesson_09_csv_scoreboard.py`)
- **Focus**: Store and load game scores from a CSV file.
- **Exercises**:
  1. **Top Three Podium**: Sort the loaded scores by `points` and print a podium for the top three students.
  2. **Append Scores**: Allow new scores to be appended to the CSV file instead of overwriting it each time.
- **Example Output**:
  ```text
  Added Mia with 25 points
  Added Kai with 19 points
  Top three:
  1. Mia - 25
  2. Alex - 22
  3. Kai - 19
  ```

### Classroom Dashboard (`advanced/lesson_10_capstone_dashboard.py`)
- **Focus**: Combine previous skills to build a tiny classroom dashboard.
- **Exercises**:
  1. **Checklist Feature**: Add a checklist feature that lets classmates mark tasks as complete and saves the status to a JSON file.
  2. **Due Date Countdown**: Display how many days remain until each due date using the `datetime` module.
- **Example Output**:
  ```text
  Science poster due in 5 days
  Saved checklist to checklist.json
  ```
