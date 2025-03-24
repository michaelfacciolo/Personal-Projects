import json
import os
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

EXPENSES_FILE = "expenses.json"


@dataclass
class Expense:
    """Dataclass to represent an expense entry."""
    description: str
    amount: float


def load_expenses() -> List[Expense]:
    """Load expenses from a JSON file with robust error handling and validation."""
    if not os.path.exists(EXPENSES_FILE):
        return []

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return [Expense(**item) for item in data if "description" in item and "amount" in item]
    except (json.JSONDecodeError, IOError, TypeError) as e:
        print(f"⚠️ Error loading expenses: {e}. Resetting file.")

    return []


def save_expenses(expenses: List[Expense]) -> None:
    """Save expenses to a JSON file, ensuring data integrity."""
    try:
        with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
            json.dump([asdict(exp) for exp in expenses], file, indent=4)
    except IOError as e:
        print(f"⚠️ Error saving expenses: {e}")


def get_valid_float(prompt: str) -> float:
    """Prompt the user for a valid positive float input."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("🚨 Amount must be a positive number. Try again.")
                continue
            return round(value, 2)
        except ValueError:
            print("🚨 Invalid input. Please enter a valid number.")


def add_expense(expenses: List[Expense]) -> None:
    """Add a new expense entry."""
    description = input("📝 Enter expense description: ").strip()
    if not description:
        print("🚨 Description cannot be empty.")
        return

    amount = get_valid_float("💰 Enter expense amount: $")
    new_expense = Expense(description, amount)
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"✅ Added: {new_expense.description} - ${new_expense.amount:.2f}")


def view_expenses(expenses: List[Expense], tail: Optional[int] = None) -> None:
    """Display all expenses or the last 'tail' number of entries."""
    if not expenses:
        print("📭 No expenses recorded.")
        return

    print("\n📌 **Expenses List**")
    expenses_to_show = expenses[-tail:] if tail else expenses
    for i, expense in enumerate(expenses_to_show, 1):
        print(f"  {i}. {expense.description} - 💵 ${expense.amount:.2f}")

    total = sum(expense.amount for expense in expenses)
    print(f"\n📊 **Total Expenses:** ${total:.2f}")


def get_valid_index(prompt: str, max_index: int) -> int:
    """Prompt the user for a valid index within range."""
    while True:
        try:
            index = int(input(prompt).strip()) - 1
            if 0 <= index < max_index:
                return index
            print(f"🚨 Invalid selection. Enter a number between 1 and {max_index}.")
        except ValueError:
            print("🚨 Invalid input. Please enter a number.")


def delete_expense(expenses: List[Expense]) -> None:
    """Delete an expense by selecting an index."""
    if not expenses:
        print("📭 No expenses to delete.")
        return

    view_expenses(expenses)
    index = get_valid_index("🗑️ Enter the expense number to delete: ", len(expenses))
    removed_expense = expenses.pop(index)
    save_expenses(expenses)
    print(f"🗑️ Deleted: {removed_expense.description} - 💵 ${removed_expense.amount:.2f}")


def exit_program() -> None:
    """Exit the program gracefully."""
    print("👋 Goodbye! Stay on top of your expenses! 🚀")
    exit()


def main() -> None:
    """Run the expense tracker application."""
    print("📒 Welcome to the **Expense Tracker** 📒")
    expenses = load_expenses()

    menu_options = {
        "1": ("➕ Add Expense", lambda: add_expense(expenses)),
        "2": ("📜 View All Expenses", lambda: view_expenses(expenses)),
        "3": ("🔍 View Last 5 Expenses", lambda: view_expenses(expenses, tail=5)),
        "4": ("🗑️ Delete Expense", lambda: delete_expense(expenses)),
        "5": ("🚪 Exit", exit_program)
    }

    while True:
        print("\n📌 **Menu:**")
        for key, (desc, _) in menu_options.items():
            print(f"  {key}. {desc}")
        choice = input("➡️ Enter your choice: ").strip()

        menu_options.get(choice, (None, lambda: print("🚨 Invalid choice. Please enter a valid option.")))[1]()


if __name__ == "__main__":
    main()