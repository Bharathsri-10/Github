def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add  task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Exit")
list1=[]
def add_task(list1):
    task = input("Enter the task description: ")
    list1.append(task)
    print(f"Task added: {task}")

def remove_task(list1):
    view_tasks(list1)
    index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= index < len(list1):
        removed_task = list1.pop(index)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task number.")

def view_tasks(list1):
    if not list1:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for i, task in enumerate(list1, 1):
            print(f"{i}. {task}")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(list1)
        elif choice == '2':
            remove_task(list1)
        elif choice == '3':
            view_tasks(list1)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
