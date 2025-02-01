# ChatGPT created this program.
import json

# To-Do List Manager class
class ToDoListManager:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from the JSON file
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Save tasks to the JSON file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Add a new task
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f'Task "{task}" added.')

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")

    # Mark a task as completed
    def complete_task(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            if not task["completed"]:
                task["completed"] = True
                self.save_tasks()
                print(f'Task "{task["task"]}" marked as completed.')
            else:
                print(f'Task "{task["task"]}" is already completed.')
        except IndexError:
            print("Invalid task number.")

    # Remove a task
    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f'Task "{task["task"]}" removed.')
        except IndexError:
            print("Invalid task number.")

# Main program
def main():
    todo_manager = ToDoListManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_manager.add_task(task)
        elif choice == '2':
            todo_manager.view_tasks()
        elif choice == '3':
            todo_manager.view_tasks()
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                todo_manager.complete_task(task_num)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '4':
            todo_manager.view_tasks()
            try:
                task_num = int(input("Enter the task number to remove: "))
                todo_manager.remove_task(task_num)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '5':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
