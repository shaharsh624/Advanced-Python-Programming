import csv
import os
import shutil
import matplotlib.pyplot as plt
from datetime import datetime

CSV_FILE='expense.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames=['Name','Date','Description','Amount','Category']
        writer=csv.DictWriter(csvfile, fieldanames=fieldnames)
        writer.writerheader()

def log_expense():
    name = input("Enter your name: ")
    date_str = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the expense description: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the expense category: ")

    try:
        date=datetime.strptime(date_str,'%Y-%m-%d')
    except ValueError:
        print("Invalid date format.")
        return
    
    with open(CSV_FILE,'a',newline='') as csvfile:
        fieldnames= ['Name', 'Date', 'Description', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Date': date_str, 'Description': description, 'Amount': amount, 'Category': category})

    print("Expense logged successfully.")

def analyze_expenses():
    total_expenses = {}
    average_daily_expense = 0
    total_days = 0

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            amount = float(row['Amount'])

            if name in total_expenses:
                total_expenses[name] += amount
            else:
                total_expenses[name] = amount

            total_days += 1

        if total_days > 0:
            average_daily_expense = sum(total_expenses.values()) / total_days

        print("Total expenses for each family member:")
        for name, expenses in total_expenses.items():
            print(f"{name}: {expenses:.2f}")

        print(f"Average daily expense for the household: {average_daily_expense:.2f}")

def generate_expense_trends():
    daily_expenses = {}

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date_str = row['Date']
            amount = float(row['Amount'])
            date = datetime.strptime(date_str, '%Y-%m-%d')

            if date in daily_expenses:
                daily_expenses[date] += amount
            else:
                daily_expenses[date] = amount

    dates = list(daily_expenses.keys())
    expenses = [daily_expenses[date] for date in dates]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, expenses, marker='o')
    plt.xlabel("Date")
    plt.ylabel("Total Expenses")
    plt.title("Expense Trends Over the Last Month")
    plt.grid()
    plt.show()

def categorize_expenses():
    with open(CSV_FILE, 'r', newline='') as csvfile:
        data = list(csv.DictReader(csvfile))

    unique_categories = set(row['Category'] for row in data)
    print("Available expense categories:")
    for idx, category in enumerate(unique_categories):
        print(f"{idx + 1}. {category}")

    expense_idx = int(input("Enter the index of the expense to categorize: "))
    category = input("Enter the category for this expense: ")

    if 1 <= expense_idx <= len(data):
        data[expense_idx - 1]['Category'] = category

        with open(CSV_FILE, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Date', 'Description', 'Amount', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("Expense categorized successfully.")
    else:
        print("Invalid expense index.")

def generate_monthly_report():
    total_expenses = {}
    expenses_by_category = {}

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            amount = float(row['Amount'])
            category = row['Category']

            if name in total_expenses:
                total_expenses[name] += amount
            else:
                total_expenses[name] = amount

            if category in expenses_by_category:
                expenses_by_category[category] += amount
            else:
                expenses_by_category[category] = amount

    current_month = datetime.now().strftime('%B %Y')

    print(f"Monthly Expense Report for {current_month}")
    print("Total expenses for each family member:")
    for name, expenses in total_expenses.items():
        print(f"{name}: {expenses:.2f}")

    print("\nBreakdown of expenses by category:")
    for category, expenses in expenses_by_category.items():
        print(f"{category}: {expenses:.2f}")

def set_budget():
    budget_data = {}

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            if category not in budget_data:
                budget = float(input(f"Enter the monthly budget for '{category}': "))
                budget_data[category] = budget

    with open('budgets.csv', 'w', newline='') as budget_file:
        writer = csv.writer(budget_file)
        writer.writerow(['Category', 'Budget'])
        for category, budget in budget_data.items():
            writer.writerow([category, budget])

    print("Budgets set successfully.")

def backup_expenses():
    try:
        backup_dir = 'backup'
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_filename = os.path.join(backup_dir, f'expenses_backup_{timestamp}.csv')
        shutil.copy(CSV_FILE, backup_filename)
        print(f"Expenses backup created: {backup_filename}")
    except Exception as e:
        print(f"Error creating backup: {str(e)}")

def restore_expenses():
    try:
        backup_files = [f for f in os.listdir('backup') if f.startswith('expenses_backup_')]
        if not backup_files:
            print("No backup files found.")
            return

        print("Available backup files:")
        for idx, filename in enumerate(backup_files):
            print(f"{idx + 1}. {filename}")

        choice = int(input("Enter the index of the backup file to restore: "))
        selected_backup = os.path.join('backup', backup_files[choice - 1])
        shutil.copy(selected_backup, CSV_FILE)
        print(f"Expenses restored from: {selected_backup}")
    except Exception as e:
        print(f"Error restoring expenses: {str(e)}")

while True:
    print("\nHousehold Expenses Tracker Menu:")
    print("1. Log Expense")
    print("2. Analyze Expenses")
    print("3. Generate Expense Trends")
    print("4. Categorize Expenses")
    print("5. Generate Monthly Report")
    print("6. Set Budget")
    print("7. Backup Expenses")
    print("8. Restore Expenses")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        log_expense()
    elif choice == '2':
        analyze_expenses()
    elif choice == '3':
        generate_expense_trends()
    elif choice == '4':
        categorize_expenses()
    elif choice == '5':
        generate_monthly_report()
    elif choice == '6':
        set_budget()
    elif choice == '7':
        backup_expenses()
    elif choice == '8':
        restore_expenses()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please choose a valid option.")