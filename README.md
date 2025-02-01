# To-Do List Manager (Python)

A simple command-line-based To-Do List Manager that allows users to manage their tasks. It provides options to add, view, complete, and remove tasks, while saving the data to a JSON file for persistence.

## Features
- Add new tasks to the To-Do list.
- View all tasks with their current status (Pending/Completed).
- Mark tasks as completed.
- Remove tasks from the list.
- Save tasks to a JSON file (`todo_list.json`), which persists even after the program is closed.

## Requirements
- Python 3.x

## Installation

1. Clone this repository or download the source code.
2. Ensure Python 3.x is installed on your system.

   ```bash
   python --version

   How to Run the Program
Open a terminal or command prompt.

Navigate to the directory where the Python file is saved.

Run the program using the following command:

bash
Copy
python todo_list_manager.py
The program will present a menu with the following options:

1. Add Task: Add a new task to the To-Do list.
2. View Tasks: View all tasks and their completion status.
3. Mark Task as Completed: Mark a task as completed.
4. Remove Task: Remove a task from the list.
5. Exit: Exit the program.
JSON File

The program saves the tasks to a todo_list.json file in the same directory as the Python script. Here's an example of how the tasks are stored:
task: The description of the task.
completed: A boolean indicating whether the task is completed (true) or not (false).

Example Usage
Sample Output
bash
Copy
To-Do List Manager
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit
Enter your choice: 1
Enter the task: Study for exams
Task "Study for exams" added.

To-Do List Manager
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit
Enter your choice: 2

To-Do List:
1. Buy groceries - Pending
2. Complete Python project - Completed
3. Study for exams - Pending
Contributing
Fork this repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your branch (git push origin feature-branch).
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

### Notes:
- This `README.md` provides a clear description of the project, instructions on installation and usage, and an example of how the JSON file is structured.
- It also includes guidelines for contributing and a reference to the license, making it more accessible for potential contributors or users.
