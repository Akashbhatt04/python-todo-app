import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks! You're all caught up.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"➕ Task added: {task}")
    else:
        print("⚠️ Cannot add an empty task.")
    print()

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"❌ Task removed: {removed}")
        else:
            print("❗Invalid task number.")
    except ValueError:
        print("❗Please enter a valid number.")
    print()

def main():
    tasks = load_tasks()
    while True:
        print("📋 To-Do List Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("❗Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
