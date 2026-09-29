expenses = []            
FILE_NAME = "expenses.txt"   


def load_expenses_from_file():
   
    file = open(FILE_NAME, "a")
    file.close()

    file = open(FILE_NAME, "r")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            category = parts[0]
            amount = float(parts[1])
            date = parts[2]
            expenses.append((category, amount, date))
    file.close()


def save_expenses_to_file():
    
    file = open(FILE_NAME, "w")
    for category, amount, date in expenses:
        file.write(category + "," + str(amount) + "," + date + "\n")
    file.close()


def add_expense():
    
    category = input("Enter expense category (e.g. Food, Travel, Rent): ")
    amount = float(input("Enter amount spent: "))

    
    if amount <= 0:
        print("Amount should be greater than zero. Expense not added.\n")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    expenses.append((category, amount, date))
    save_expenses_to_file()
    print("Added: " + category + " - Rs." + str(amount) + " on " + date + "\n")


def view_all_expenses():
    
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    count = 1
    for category, amount, date in expenses:
        print(str(count) + ". " + category + " - Rs." + str(amount) + " on " + date)
        count = count + 1
    print()


def category_summary():
    
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return {}

    summary = {}   

    for category, amount, date in expenses:
        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    print("\n--- Category-wise Summary ---")
    for category in summary.keys():
        print(category + ": Rs." + str(summary[category]))

    total = 0
    for amount in summary.values():
        total = total + amount
    print("Total spent so far: Rs." + str(total) + "\n")

    return summary


def highest_and_lowest_category():
    
    summary = category_summary()

    if len(summary) == 0:
        return

    max_category = ""
    min_category = ""
    max_amount = 0
    min_amount = None

    for category in summary.keys():
        amount = summary[category]

        if amount > max_amount:
            max_amount = amount
            max_category = category

        if min_amount is None or amount < min_amount:
            min_amount = amount
            min_category = category

    print("Highest spending category: " + max_category + " (Rs." + str(max_amount) + ")")
    print("Lowest spending category: " + min_category + " (Rs." + str(min_amount) + ")\n")


def search_by_category():
    
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return

    category = input("Enter category to search: ")

    
    matches = [item for item in expenses if item[0] == category]

    if len(matches) == 0:
        print("No expenses found under '" + category + "'.\n")
        return

    print("\n--- Expenses under " + category + " ---")
    for c, amount, date in matches:
        print("Rs." + str(amount) + " on " + date)
    print()


def main():
    
    load_expenses_from_file()
    print("Welcome to your Daily Expense Tracker!\n")

    while True:
        print("========= DAILY EXPENSE TRACKER =========")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Category-wise summary")
        print("4. Highest & lowest spending category")
        print("5. Search expenses by category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            highest_and_lowest_category()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting the Expense Tracker. See you tomorrow!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


main()