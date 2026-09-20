"""Password strength checker.



Sample:

    Enter password: hello

    Strength: Weak | Missing: uppercase letter, number, special character, 8+ characters

    Enter password: Super@2026

    Strength: Strong | Missing: nothing

"""

import string





def check_password_strength(password):

    """Return (strength_label, list_of_missing_requirements)."""

    has_upper = has_lower = has_digit = has_special = False



    for char in password:

        if char.isupper():

            has_upper = True

        elif char.islower():

            has_lower = True

        elif char.isdigit():

            has_digit = True

        elif char in string.punctuation:

            has_special = True



    long_enough = len(password) >= 8



    checks = [

        (has_upper, "uppercase letter"),

        (has_lower, "lowercase letter"),

        (has_digit, "number"),

        (has_special, "special character"),

        (long_enough, "8+ characters"),

    ]



    score = 0

    missing = []

    for passed, description in checks:

        if passed:

            score += 1

        else:

            missing.append(description)



    if score == 5:

        label = "Strong"

    elif score == 4:

        label = "Good"

    elif score == 3:

        label = "Medium"

    else:

        label = "Weak"

    return label, missing





def main():

    while True:

        password = input("\nEnter password (or 'q' to quit): ")

        if password.lower() == "q":

            print("Goodbye!")

            break

        if not password:

            print("Password cannot be empty.")

            continue

        label, missing = check_password_strength(password)

        print(f"Strength: {label}")

        print("Missing :", ", ".join(missing) if missing else "nothing")





if __name__ == "__main__":

    main()
