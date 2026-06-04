print("Expense Tracker")

total = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        total += float(expense)
    except ValueError:
        print("Please enter a valid number.")

print("Total Spent:", total)
