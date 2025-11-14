# Python Lesson Roadmap

This repository is organized into three learning tracks (beginner, intermediate, advanced). Run each lesson file to see a guided demo, then complete the matching exercises below. Ask your coach for any hints or help!

## Beginner Track

Beginner lessons now live in themed folders (basics, loops, functions, data, input). Work through each topic in order to build confidence before moving to the intermediate track.

### Basics
Foundational skills for working with numbers, types, and comparisons.

#### Variables & Numbers (`beginner/basics/lesson_variables_numbers.py`)
- **Focus**: Manage integers and floats to track classroom progress.
- **Exercises**:
  1. Track completed and remaining lessons, then print a friendly progress bar.
  2. Convert study minutes to hours with a formatted sentence.
- **Example Output**:
  ```text
  Progress: 3/10 lessons (30.0%)
  Study time: 90 minutes = 1.5 hours
  ```

#### Data Type Detective (`beginner/basics/lesson_data_types.py`)
- **Focus**: Recognize Python data types and convert between them.
- **Exercises**:
  1. Build a list containing an int, float, string, and bool, then print each value with its type.
  2. Turn a numeric string into an int and add it to a float to show the total.
- **Example Output**:
  ```text
  Value 42 -> int
  Value 'projects' -> str
  Combined total: 55.5
  ```

#### Helpful Conditionals (`beginner/basics/lesson_conditionals.py`)
- **Focus**: Write if/elif/else chains for guidance and validation.
- **Exercises**:
  1. Create a weather_helper(temp_c) that returns what to wear.
  2. Extend grade logic to reject scores less than 0 or over 100 before grading.
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
  1. Print a multiplication table for numbers 1 through 5.
  2. Iterate over a chores list and number each task using enumerate.
- **Example Output**:
  ```text
  1 x 5 = 5
  2 x 5 = 10
  Task 1: Feed the fish
  ```

#### While-Loop Control (`beginner/loops/lesson_while_loops.py`)
- **Focus**: Build while-loops with sentinels and counters.
- **Exercises**:
  1. Prompt for commands until the user types "exit".
  2. Create a countdown timer that prints "Time!" at the end.
- **Example Output**:
  ```text
  Command> practice
  Command> exit
  Countdown: 3 2 1 Time!
  ```

#### Nested Loop Grids (`beginner/loops/lesson_nested_loops.py`)
- **Focus**: Layer loops to build grids or tables.
- **Exercises**:
  1. Print coordinates for a 3x3 tic-tac-toe board.
  2. Store multiplication results in a list of lists and display them nicely.
- **Example Output**:
  ```text
  (row 1, col 1)
  (row 1, col 2)
  Grid row: [1, 2, 3]
  ```


### Function Workshop
Create reusable helpers with parameters, return values, and docstrings.

#### Function Greetings (`beginner/functions/lesson_intro_functions.py`)
- **Focus**: Define and call simple functions that format strings.
- **Exercises**:
  1. Write greet_student(name, goal) that returns a motivational string.
  2. Add an optional grade_level parameter with a default value and show how it changes the output.
- **Example Output**:
  ```text
  Hello Skyler! Keep working toward mastering loops.
  Hello Skyler (Grade 7)!
  ```

#### Return Values (`beginner/functions/lesson_parameters_returns.py`)
- **Focus**: Collect input values, compute results, and return summaries.
- **Exercises**:
  1. Implement calc_average(scores) that returns the mean of three quiz scores.
  2. Write make_badge(name, club="Coding Crew") that formats a badge label.
- **Example Output**:
  ```text
  Average score: 88.7
  Badge -> Skyler | Coding Crew
  ```

#### Docstrings & Imports (`beginner/functions/lesson_docstrings_modules.py`)
- **Focus**: Explain functions with docstrings and reuse standard modules.
- **Exercises**:
  1. Add docstrings to each helper describing parameters and returns.
  2. Import math or statistics to compute circle area and quiz averages inside functions.
- **Example Output**:
  ```text
  Circle area (r=3): 28.27
  Quiz mean: 92.0
  ```


### Data Structures
Organize information with lists, dictionaries, sets, and tuples.

#### List Playground (`beginner/data/lesson_lists.py`)
- **Focus**: Slice, append, and summarize lists of lesson data.
- **Exercises**:
  1. Store lesson durations and compute the total hours.
  2. Simulate a help-desk queue using insert and pop operations.
- **Example Output**:
  ```text
  Durations: [0.5, 0.75, 1.0] -> 2.25h
  Queue after pop: ["Loops", "Projects"]
  ```

#### Dictionary Dashboards (`beginner/data/lesson_dictionaries.py`)
- **Focus**: Map keys to values for tracking student progress.
- **Exercises**:
  1. Create a nested dictionary of modules -> completion percent.
  2. Write describe_student(data) that returns "Name (level) - N modules".
- **Example Output**:
  ```text
  loops: 60%
  functions: 80%
  Skyler (beginner) - 3 modules
  ```

#### Sets & Tuples (`beginner/data/lesson_sets_tuples.py`)
- **Focus**: Use sets for uniqueness and tuples for ordered pairs.
- **Exercises**:
  1. Collect club names in a set to remove duplicates.
  2. Store classroom seat coordinates as tuples and iterate over them.
- **Example Output**:
  ```text
  Unique clubs: {'Robotics', 'Chess'}
  (row=1, seat=B)
  ```


### Input & Files
Format text, gather user input, and read/write simple files.

#### String Stylizer (`beginner/io/lesson_strings.py`)
- **Focus**: Clean user text and combine it with f-strings.
- **Exercises**:
  1. Strip whitespace from a name and print a title-cased greeting.
  2. Split a comma list of favorite topics and rejoin them with arrows.
- **Example Output**:
  ```text
  Welcome, Aarya!
  loops -> games -> art
  ```

#### Friendly File I/O (`beginner/io/lesson_file_io.py`)
- **Focus**: Save notes to disk and read them back with numbering.
- **Exercises**:
  1. Write three motivational lines to a text file and number them when printing.
  2. Wrap save/load actions in helper functions for reuse.
- **Example Output**:
  ```text
  1. Keep practicing.
  2. Test often.
  Loaded notes successfully.
  ```

#### Interactive Quiz (`beginner/io/lesson_user_input.py`)
- **Focus**: Gather input safely and provide instant feedback.
- **Exercises**:
  1. Build a two-question math quiz that scores the player.
  2. Validate numeric answers before converting them to int or float.
- **Example Output**:
  ```text
  What is 4 + 3? Correct!
  Score: 2/2
  ```

## Intermediate Track

Skills build lesson by lesson start at 01 and keep going. Each entry lists the main idea, follow-up exercises, and a captured snippet of console output so you know what success looks like.

### List Comprehensions (`intermediate/lesson_01_list_comprehensions.py`)
- **Focus**: Transform sequences with list comprehensions.
- **Exercises**:
  1. Replace the list comprehension with an equivalent for-loop and compare readability.
  2. Build a dictionary comprehension that maps numbers 1-5 to their cubes.
- **Example Output**:
  ```text
  Comprehension: [1, 4, 9, 16, 25]
  Manual loop: [1, 4, 9, 16, 25]
  {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
  ```

### Error Handling (`intermediate/lesson_02_error_handling.py`)
- **Focus**: Use try/except/else/finally blocks.
- **Exercises**:
  1. Raise a ValueError inside safe_divide when non-numeric arguments are provided.
  2. Write a context manager that logs when division starts/ends and pair it with try/except.
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
  1. Add a limit parameter to id_sequence that stops iteration and raises StopIteration with a message.
  2. Create a generator expression that yields only even IDs from the main generator.
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
  1. Extend log_call to measure execution time using time.perf_counter.
  2. Write a second decorator that caches the result of a pure function and compose it with log_call.
- **Example Output**:
  ```text
  slow_add took 0.10s
  Result: 5
  slow_add took 0.00s (cache hit)
  ```

### Classes & Objects (`intermediate/lesson_05_classes.py`)
- **Focus**: Use classes to encapsulate behavior.
- **Exercises**:
  1. Add a level_up method that upgrades the difficulty and returns self for chaining.
  2. Create a subclass VideoLesson that stores runtime minutes and overrides describe.
- **Example Output**:
  ```text
  Classes (advanced)
  Decorators (intermediate) - 12 minutes
  ```

### Dataclasses (`intermediate/lesson_06_dataclasses.py`)
- **Focus**: Leverage dataclasses for simple models.
- **Exercises**:
  1. Add a computed property that returns a slugified version of the assignment title.
  2. Instantiate several Assignment objects and sort them by max_score using sorted and attrgetter.
- **Example Output**:
  ```text
  Slug -> loops-drill
  Sorted: [Assignment(title='Loops Drill', max_score=30), Assignment(title='Dataclasses', max_score=50)]
  ```

### Type Hints (`intermediate/lesson_07_type_hints.py`)
- **Focus**: Add static typing hints and TypedDict usage.
- **Exercises**:
  1. Annotate tag_lesson to accept Sequence[str] instead of List[str] and explain why.
  2. Create a Protocol representing a renderer with a render(title: str) -> str method and implement two versions.
- **Example Output**:
  ```text
  Decorators => functions, wrappers
  *** Type hints ***
  PROTOCOLS ROCK
  ```

### Context Managers (`intermediate/lesson_08_context_managers.py`)
- **Focus**: Create custom context managers.
- **Exercises**:
  1. Write a context manager class (not decorator) that times how long a block takes to run.
  2. Refactor open_lesson to accept a mode parameter and test both write and read flows.

### Logging Basics (`intermediate/lesson_09_logging.py`)
- **Focus**: Configure logging for reusable modules.
- **Exercises**:
  1. Configure a file handler that writes logs to logs/intermediate.log.
  2. Add structured data (e.g., lesson name, user) to the log message using keyword arguments.

### Testing Primer (`intermediate/lesson_10_testing.py`)
- **Focus**: Show a pytest-style test function.
- **Exercises**:
  1. Split add into a new module and import it inside the test to mimic real project structure.
  2. Parametrize test_add to cover negative numbers and zero using pytest.mark.parametrize syntax (document it in comments).
- **Example Output**:
  ```text
  All test cases passed!
  ```


## Advanced Track

Skills build lesson by lesson start at 01 and keep going. Each entry lists the main idea, follow-up exercises, and a captured snippet of console output so you know what success looks like.

### Study Timer (`advanced/lesson_01_study_timer.py`)
- **Focus**: Build a friendly study timer that breaks sessions into focus and rest blocks.
- **Exercises**:
  1. Ask the user how long they want to focus and rest, then run the timer with their choices.
  2. Add encouraging messages ("Great job!", "Grab water!") every time a block finishes.
- **Example Output**:
  ```text
  Focus: 30 seconds left
  Focus block complete! Great job!
  Break: 15 seconds left
  ```

### Math Quiz (`advanced/lesson_02_math_quiz.py`)
- **Focus**: Create a mini math quiz game that tracks the score for each player.
- **Exercises**:
  1. Let players answer with input() and give hints if they are close to the correct answer.
  2. Store each player's score in a dictionary so you can display a leaderboard at the end.
- **Example Output**:
  ```text
  What is 5 + 7? -> Correct!
  What is 3 + 8? -> Close, try again!
  Leaderboard:
  Maya: 3
  ```

### Flashcard Helper (`advanced/lesson_03_flashcard_app.py`)
- **Focus**: Model a simple flashcard helper using dictionaries and loops.
- **Exercises**:
  1. Shuffle the flashcards and quiz the player by only showing the term first.
  2. Save the cards to a text file so classmates can load them later.
- **Example Output**:
  ```text
  Term: Planet?
  A big ball in space that orbits a star.
  Saved 3 cards to flashcards.txt
  ```

### Budget Tracker (`advanced/lesson_04_budget_tracker.py`)
- **Focus**: Track weekly allowance spending with lists and simple calculations.
- **Exercises**:
  1. Ask the user for their allowance and warn them when only $5 remains.
  2. Sort purchases from most to least expensive before printing the summary.
- **Example Output**:
  ```text
  Warning! Only $4.75 left.
  Book: $8.00
  Snacks: $3.25
  ```

### Club Roster (`advanced/lesson_05_club_roster.py`)
- **Focus**: Use classes to organize a school club roster.
- **Exercises**:
  1. Add a method that searches for members by role and prints their names.
  2. Create a `SportsClub` subclass that tracks the sport name and overrides `badge_text`.
- **Example Output**:
  ```text
  Mina - Grade 9 (Captain)
  Leo - Soccer (Player)
  ```

### Weather Report (`advanced/lesson_06_weather_report.py`)
- **Focus**: Summarize weekly weather using dictionaries and helper functions.
- **Exercises**:
  1. Convert the temperatures to Celsius and show both scales in the summary.
  2. Ask the user which day they want a report for and print the high/low pair.
- **Example Output**:
  ```text
  Mon: High 72°F/22.2°C, Low 60°F/15.6°C
  Tue: High 75°F/23.9°C, Low 62°F/16.7°C
  ```

### Schedule Planner (`advanced/lesson_07_schedule_planner.py`)
- **Focus**: Build a day planner that keeps tasks in order.
- **Exercises**:
  1. Let the user remove a task by typing its time.
  2. Export the ordered plan to a file called `my_schedule.txt`.
- **Example Output**:
  ```text
  Removed tasks at 09:00
  Saved schedule to my_schedule.txt
  ```

### Guessing Game (`advanced/lesson_08_guess_game.py`)
- **Focus**: Code a number guessing game with friendly hints.
- **Exercises**:
  1. Replace the pretend guesses with input() and keep looping until the player wins.
  2. Track how many guesses were used and celebrate if they solved it in three tries or less.
- **Example Output**:
  ```text
  Too low!
  Too high!
  You got it in 3 guesses!
  ```

### CSV Scoreboard (`advanced/lesson_09_csv_scoreboard.py`)
- **Focus**: Store and load game scores from a CSV file.
- **Exercises**:
  1. Sort the loaded rows by `points` and print a podium for the top three students.
  2. Allow new scores to be appended instead of overwriting the whole file each time.
- **Example Output**:
  ```text
  Added Mia with 25 points
  Added Kai with 19 points
  Top three:
  Mia - 25
  ```

### Classroom Dashboard (`advanced/lesson_10_capstone_dashboard.py`)
- **Focus**: Combine previous skills to build a tiny classroom dashboard.
- **Exercises**:
  1. Add a checklist feature that lets classmates mark tasks complete and saves the status to a file.
  2. Display how many days remain until each due date using the datetime module.
- **Example Output**:
  ```text
  Science poster due in 5 days
  Saved checklist to checklist.json
  ```
