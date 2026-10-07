from database import Database
from task import Task


db = Database()
db.create_table()

print("=== AI STUDENT PLANNER ===")
print("1. Add task")
print("2. Search by subject")
print("3. Search by priority")

choice = input("Choose option: ")

if choice == "1":
    title = input("Title: ")
    subject = input("Subject: ")
    description = input("Description: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    priority = input("Priority (Low/Medium/High): ")

    task = Task(
        title,
        subject,
        description,
        deadline,
        priority
    )

    db.insert_task(task)

    print("Task added successfully!")

elif choice == "2":
    subject = input("Enter subject: ")

    tasks = db.select_tasks_by_subject(subject)

    print("\n=== RESULTS ===")

    for task in tasks:
        print(task)

elif choice == "3":
    priority = input("Enter priority (Low/Medium/High): ")

    tasks = db.select_tasks_by_priority(priority)

    print("\n=== RESULTS ===")

    for task in tasks:
        print(task)

else:
    print("Invalid option.")


