# To Do List Application

def welcome_message(name):
  """Prints a welcome message with the given name."""
  print(f"Hello, {name}! Welcome to the To-Do List App.!")

def add_task(to_do_list):
    task = input("Enter task to add: ")
    to_do_list.append(task)

def remove_task(to_do_list):
    task = input("Enter item to remove: ")
    if task in to_do_list:
        to_do_list.remove(task)
    else:
        print(f"{task} not found in the list.")

def print_list(to_do_list):
    print("\nTo Do List:")
    if not to_do_list:
        print("Your to do list is empty.")
    else:
        for i, task in enumerate(to_do_list):
            print(f"{i+1}. {task}")

to_do_list = ["Exercise", "Prepare", "Commute", "Work", 
"Commute", "Read & Listen To Music"]

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        print_list(to_do_list)
    elif choice == "3":
        def complete_task(task):
            if task in to_do_list:
                tasks.remove(task)
                print(f"Task '{task}' marked as completed!")
else:
        print(f"Task '{task}' not found.")
        if choice == "4":
            remove_task(to_do_list)
if choice == "5":
    exit()
else:
        print("Invalid choice.")

try:
    result = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
except ValueError:
    print("Invalid input. Please enter a valid task.")
else:
    print("You have entered a task.")
finally:
    print("You have entered a task")