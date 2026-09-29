# # Daily Expense Tracker

## Overview
A simple menu-driven Python program that helps track daily expenses.
Users can add expenses under categories (like Food, Travel, Rent), view
all recorded expenses, get a category-wise summary of spending, find the
highest and lowest spending categories, and search expenses by category.

## Features
- Add a new expense with category, amount, and date
- View all recorded expenses
- Category-wise spending summary with total
- Identify the highest and lowest spending categories
- Search expenses by category
- Basic input validation (rejects zero or negative amounts)

## Technologies / Tools Used
- Python 3
- Core concepts: Lists, Tuples, Dictionaries, Loops, Conditionals,
  Functions, List Comprehension, File Handling (read/write)

## Project Structure
```
daily-expense-tracker/
├── expense_tracker.py
├── README.md
└── statement.md
```

## Steps to Install & Run
1. Make sure Python 3 is installed on your system. Check with:
   ```
   python3 --version
   ```
2. Clone this repository:
   ```
   git clone <https://github.com/Krishn892/Daily.expense_tracker>
   cd daily-expense-tracker
   ```
3. Run the program:
   ```
   python3 expense_tracker.py
   ```

## Instructions for Testing
1. Run the program using the steps above.
2. Choose option 1 to add a few sample expenses, for example:
   - Food, 250, 26-09-2026
   - Travel, 1200, 25-09-2026
3. Choose option 2 to view all expenses and confirm they were saved.
4. Choose option 3 to see the category-wise summary and total spending.
5. Choose option 4 to check the highest and lowest spending categories.
6. Choose option 5 and enter a category name to search expenses under it.
7. Enter an invalid menu choice (e.g. 9) to confirm it is handled gracefully.
8. Choose option 6 to exit the program.

## Note on Data
Expenses are saved to a file called `expenses.txt` in the same folder
as the program. This file is created automatically the first time you
run the program, and every new expense is written to it immediately,
so your data is still there the next time you run the tracker.
