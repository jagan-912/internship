import os
import json
from collections import defaultdict
from datetime import datetime

# Constants
DATA_FILE = "expenses.json"

# Function to load expense data from file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return defaultdict(list)
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Function to save expense data to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file)

# Function to record an expense
def record_expense(expenses):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category: ")
    date_str = input("Enter date (YYYY-MM-DD), leave empty for today: ")
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Check if category exists, if not create it
    if category not in expenses:
        expenses[category] = []
    
    expenses[category].append({"amount": amount, "description": description, "date": date_str})
    save_expenses(expenses)
    print("Expense recorded successfully!")

# Function to display monthly expenses summary
def monthly_summary(expenses):
    current_month = datetime.now().strftime("%Y-%m")
    total_expenses = 0
    print(f"Monthly Summary for {current_month}:")
    for category, items in expenses.items():
        category_total = sum(item['amount'] for item in items if item['date'].startswith(current_month))
        total_expenses += category_total
        print(f"{category}: ${category_total:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")

# Function to display category-wise expenditure
def category_summary(expenses):
    print("Category-wise Expenditure:")
    for category, items in expenses.items():
        category_total = sum(item['amount'] for item in items)
        print(f"{category}: ${category_total:.2f}")

# Function to handle user interaction
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record an Expense")
        print("2. Monthly Expenses Summary")
        print("3. Category-wise Expenditure")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            record_expense(expenses)
        
        elif choice == '2':
            monthly_summary(expenses)
        
        elif choice == '3':
            category_summary(expenses)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

