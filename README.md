
# 🤓 QUIZ GAME!! — Ava's HTML, CSS and JavaScript Project Specification

**Format:** Web-based quiz game (kinda like kahoot!)
**Goal:** The goal is to build a quiz game, and a quiz editor, so you can share the quizes you make to other people using a JSON file. 

## Email for help: 
aarya.dave123@gmail.com

---

## 🎯 Learning Outcomes
By the end of the project, students will:
- Use variables, conditionals, loops, and functions  
- Manage lists, hashmaps, and JSON files!
- Create a scoring algorithm
- Use file input/output for saving and loading different quizes!
- Plan and test code iteratively  
- Write and debug readable, modular programs

---

## 🧩 Week-by-Week Breakdown (Ask me [Aarya] for any help if you need)

### Week 1 — GIT, Welcome & Home Page
Get your github stuff fully setup and working!!!
Display a home page using HTML and CSS 
- Display a home page that has the buttons "Start", "Create", "Play!"
- Clicking those buttons should take you to another Page
    - You can do this using a "hide" class if you want, or by creating another file and rerouting the user to the contents of that file
**Milestone:** Home page displays correctly and has the right functionality

### Week 2 — Input Gathering and creating the "Create Page"
This week, our goal is to make the input page for our create game page!
Display a create game page using HTML and CSS 
- Display a create game page that has the buttons "Create" and "Add question"
- Add input fields for elements you think should be in a quiz, e.g. "What is the name of this quiz?"
- Add a button that allows the user to add another question
- Find a way to signal what option in the question is correct
**Milestone:** Create game page displays and takes in inputs correctly. The "add question" button logic works such that once clicked, more input options should appear allowing the user to add extra questions to their quiz.

### Week 3-4 — Parsing our input variables into JSON
Over the next two weeks, our goal is to learn what JSON is, and apply it into the project!
Parse the input into a JSON file, that can be downloaded!
- Take the input from the "create game page" from last week and output the variables into a JSON file format!
Here is a [video to help explain JSON](https://www.youtube.com/watch?v=iiADhChRriM)
Here is an example of a JSON schema!
```JSON
{
  "quizTitle": "General Knowledge Quiz",
  "description": "A short quiz to test your general knowledge.",
  "questions": [
    {
      "id": 1,
      "questionText": "What is the capital of France?",
      "options": [
        "Berlin",
        "Madrid",
        "Paris",
        "Rome"
      ],
      "correctAnswerIndex": 2,
      "explanation": "Paris is the capital and most populous city of France."
    },
    {
      "id": 2,
      "questionText": "Which planet is known as the Red Planet?",
      "options": [
        "Venus",
        "Mars",
        "Jupiter",
        "Saturn"
      ],
      "correctAnswerIndex": 1,
      "explanation": "Mars appears red due to iron oxide on its surface."
    },
    {
      "id": 3,
      "questionText": "Who wrote 'To Kill a Mockingbird'?",
      "options": [
        "Harper Lee",
        "Mark Twain",
        "Jane Austen",
        "J.K. Rowling"
      ],
      "correctAnswerIndex": 0,
      "explanation": "Harper Lee published the novel in 1960."
    }
  ],
  "settings": {
    "shuffleQuestions": true,
    "shuffleOptions": true,
    "timeLimitSeconds": 120,
    "passingScore": 70
  }
}
```
#### Week 4
- Create a button, and pass in the given helper function to create a downloadable file.
    - This file should allow the user to download the quiz data, which will help us share the quiz later on in this project!
- Create this button in the createPage.html file
**Milestone:** Learn how JSON works, and understand how to create files in JavaScript

### Week 5 — Creating the template for the play page!
The goal of this week is to create a basic style and layout for the playPage. This is the page where users will get the question and have the ability to answer!

---

### Weekly Check (2–3 min)
- [] Runs without crashing  
- [] Weekly feature works  
- [] At least one commit made to github, and one push of working code!

---

