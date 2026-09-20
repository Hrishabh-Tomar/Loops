"""Super30 Utility App: 6 utilities in one menu.



Sample:

    Choice: 2 -> Enter text: Madam -> 'Madam' is a palindrome.

"""





def read_int(prompt):

    """Read an integer, or return None if invalid."""

    try:

        return int(input(prompt))

    except ValueError:

        print("Please enter a whole number.")

        return None





def calculator():

    """Basic two-number calculator."""

    try:

        a = float(input("First number: "))

        b = float(input("Second number: "))

    except ValueError:

        print("Invalid number.")

        return

    operator = input("Operator (+, -, *, /): ").strip()

    if operator == "+":

        print("Result:", a + b)

    elif operator == "-":

        print("Result:", a - b)

    elif operator == "*":

        print("Result:", a * b)

    elif operator == "/":

        print("Result:", "Cannot divide by zero" if b == 0 else a / b)

    else:

        print("Invalid operator.")





def palindrome_checker():

    """Check if text reads the same backwards (ignores case and spaces)."""

    text = input("Enter text: ")

    cleaned = "".join(char.lower() for char in text if char.isalnum())

    if cleaned and cleaned == cleaned[::-1]:

        print(f"'{text}' is a palindrome.")

    else:

        print(f"'{text}' is not a palindrome.")





def prime_checker():

    """Check whether a number is prime."""

    number = read_int("Enter a number: ")

    if number is None:

        return

    if number < 2:

        print(f"{number} is not prime.")

        return

    divisor = 2

    while divisor * divisor <= number:

        if number % divisor == 0:

            print(f"{number} is not prime (divisible by {divisor}).")

            return

        divisor += 1

    print(f"{number} is prime.")





def factorial_calculator():

    """Calculate the factorial of a non-negative integer."""

    number = read_int("Enter a number: ")

    if number is None:

        return

    if number < 0:

        print("Factorial is not defined for negative numbers.")

        return

    result = 1

    counter = number

    while counter > 1:

        result *= counter

        counter -= 1

    print(f"{number}! = {result}")





def multiplication_table():

    """Print the table of a number up to 10."""

    number = read_int("Enter a number: ")

    if number is None:

        return

    for i in range(1, 11):

        print(f"{number} x {i:>2} = {number * i}")





def temperature_converter():

    """Convert Celsius to Fahrenheit or the reverse."""

    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")

    choice = input("Enter choice: ").strip()

    try:

        value = float(input("Enter temperature: "))

    except ValueError:

        print("Invalid temperature.")

        return

    if choice == "1":

        print(f"{value}Â°C = {value * 9 / 5 + 32:.2f}Â°F")

    elif choice == "2":

        print(f"{value}Â°F = {(value - 32) * 5 / 9:.2f}Â°C")

    else:

        print("Invalid choice.")





def main():

    utilities = {

        "1": ("Calculator", calculator),

        "2": ("Palindrome Checker", palindrome_checker),

        "3": ("Prime Checker", prime_checker),

        "4": ("Factorial Calculator", factorial_calculator),

        "5": ("Multiplication Table", multiplication_table),

        "6": ("Temperature Converter", temperature_converter),

    }



    running = True

    while running:

        print("\n===== Super30 Utility App =====")

        for key, (title, _) in utilities.items():

            print(f"{key}. {title}")

        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()



        if choice in utilities:

            utilities[choice][1]()        # call the selected function

        elif choice == "7":

            print("Goodbye!")

            running = False

        else:

            print("Invalid choice. Please select 1-7.")





if __name__ == "__main__":

    main()
