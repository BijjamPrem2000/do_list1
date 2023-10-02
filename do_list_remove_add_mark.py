def main_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")

# You can add more functions for each menu option later.
def add_task():
    task_paragraph = input("Enter a new task: ")
    tasks = task_paragraph.split(",")
    with open("tasks.txt", "a") as file:
        #open the file tasks.txt and append the data("a") name it as the "file" :
        # "with" command is used to close the file completely after the tasks are done
        for task in tasks:
            file.write(task + "\n")
        #we write the lines in the tasks.txt in a new line every time
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:#"r" performs the read operation
            tasks = file.readlines()# the read files are stored in the tasks
            if tasks:#check the condition if the tasks are full or empty
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    #This line starts a loop that iterates through each task in the tasks list.
                    # The enumerate function is used to get both the task and its index.
                    # The start=1 argument specifies that the index should start from 1 instead of 0.
                    print(f"{i}. {task.strip()}")
                    #The strip() method is used to remove any leading or trailing whitespace (including the newline character) from the task
            else:
                print("No tasks found.")
    except FileNotFoundError:#file not found error
        print("No tasks found.")
def mark_completed():
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("tasks.txt", "r+") as file:# the "r+"  is used to perform both read and write operation
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = "[X] " + tasks[task_number - 1]
                file.seek(0)#moves the file cursor to the beginning of the file.
                file.writelines(tasks)#This line writes the modified tasks list back to the "tasks.txt" file,
                #effectively updating the task list with the completed task.
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
    except ValueError:#incorrect value entered
        print("Invalid input. Please enter a valid task number.")
def remove_task():
    try:
        task_numbers = input("Enter the task number(s) to remove (comma-separated): ")
        task_numbers = [int(num) for num in task_numbers.split()]  # Convert input to a list of integers
        task_numbers.sort(reverse=True)
        print(task_numbers)
        with open("tasks.txt", "r+") as file:
            tasks = file.readlines()
            # Initialize a list to store removed tasks for later display
            removed_tasks = []
            t=len(tasks)
            for task_number in task_numbers:
                if 1 <= task_number <= t:
                    removed_task = tasks.pop(task_number - 1)
                    removed_tasks.append(removed_task.strip())  # Add removed task to the list
                else:
                    print(f"Invalid task number: {task_number}")
            # Move the file cursor to the beginning, write updated tasks, and truncate the file
            file.seek(0)
            file.writelines(tasks)
            file.truncate()
            # Display the removed tasks
            for removed_task in removed_tasks:
                print(f"Removed task: {removed_task}")
    except ValueError:
        print("Invalid input. Please enter valid task number(s) separated by commas.")

if __name__ == "__main__":
    while True:
        main_menu()
        choice =input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
