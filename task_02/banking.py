"""Menu-driven banking application.



Sample:

    Choice: 2 -> Deposit amount: 500 -> Deposited 500.00. Balance: 1500.00

"""





def read_amount(prompt):

    """Read a positive number from the user, or return None if invalid."""

    try:

        amount = float(input(prompt))

    except ValueError:

        print("Invalid amount. Please enter a number.")

        return None

    if amount <= 0:

        print("Amount must be greater than 0.")

        return None

    return amount





def check_balance(balance):

    """Display the current balance."""

    print(f"Current balance: {balance:.2f}")





def deposit(balance, history):

    """Add money to the balance and log the transaction."""

    amount = read_amount("Enter deposit amount: ")

    if amount is None:

        return balance

    balance += amount

    history.append(f"Deposited {amount:.2f} | Balance: {balance:.2f}")

    print(f"Deposited {amount:.2f}. Balance: {balance:.2f}")

    return balance





def withdraw(balance, history):

    """Remove money from the balance if funds are sufficient."""

    amount = read_amount("Enter withdrawal amount: ")

    if amount is None:

        return balance

    if amount > balance:

        print("Insufficient balance.")

        return balance

    balance -= amount

    history.append(f"Withdrew   {amount:.2f} | Balance: {balance:.2f}")

    print(f"Withdrew {amount:.2f}. Balance: {balance:.2f}")

    return balance





def show_history(history):

    """Print every transaction so far."""

    if not history:

        print("No transactions yet.")

        return

    print("--- Transaction History ---")

    for number, entry in enumerate(history, start=1):

        print(f"{number}. {entry}")





def main():

    balance = 1000.0

    history = []

    running = True                        # loop control flag



    while running:

        print("\n--- Bank Menu ---")

        print("1. Check Balance\n2. Deposit\n3. Withdraw")

        print("4. Transaction History\n5. Exit")

        choice = input("Enter choice (1-5): ").strip()



        if choice == "1":

            check_balance(balance)

        elif choice == "2":

            balance = deposit(balance, history)

        elif choice == "3":

            balance = withdraw(balance, history)

        elif choice == "4":

            show_history(history)

        elif choice == "5":

            print("Thank you for banking with us. Goodbye!")

            running = False               # termination

        else:

            print("Invalid choice. Please select 1-5.")





if __name__ == "__main__":

    main()
