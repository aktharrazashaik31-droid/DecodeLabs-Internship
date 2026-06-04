print("To-Do List")

tasks = []

while True:
    task = input("Enter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour Tasks:")

for task in tasks:
    print("-", task)
