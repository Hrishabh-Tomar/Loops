"""Menu-driven expense tracker."""





def add_expense(expenses):

    """Read and store one named expense."""

    name = input("Expense name: ").strip()

    if not name:

        print("Expense name cannot be empty.")

        return

    try:

        amount = float(input("Amount: "))

    except ValueError:

        print("Please enter a valid amount.")

        return

    if amount < 0:

        print("Amount cannot be negative.")

        return

    expenses.append({"name": name, "amount": amount})

    print("Expense added.")





def view_expenses(expenses):

    """Display all recorded expenses."""

    if not expenses:

        print("No expenses recorded.")

        return

    for number, expense in enumerate(expenses, start=1):

        print(f"{number}. {expense['name']}: {expense['amount']:.2f}")





def calculate_total(expenses):

    """Return the total of all expense amounts."""

    total = 0

    for expense in expenses:

        total += expense["amount"]

    return total





def find_highest_expense(expenses):

    """Return the largest expense, or None when the list is empty."""

    highest = None

    for expense in expenses:

        if highest is None or expense["amount"] > highest["amount"]:

            highest = expense

    return highest





def main():

    expenses = []

    while True:

        print("\n--- Expense Tracker ---")

        print("1. Add expense\n2. View expenses\n3. Calculate total")

        print("4. Find highest expense\n5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            print(f"Total expenses: {calculate_total(expenses):.2f}")

        elif choice == "4":

            highest = find_highest_expense(expenses)

            if highest is None:

                print("No expenses recorded.")

            else:

                print(f"Highest expense: {highest['name']} ({highest['amount']:.2f})")

        elif choice == "5":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")





if __name__ == "__main__":

    main()
