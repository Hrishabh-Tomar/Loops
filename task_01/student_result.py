"""Student Result Management System.



Sample:

    Enter student name: Asha

    Enter marks for Maths (0-100): 78

    ...

    Total: 385.0 / 500 | Percentage: 77.00% | Grade: B | Result: PASS

"""



SUBJECTS = ["Maths", "Science", "English", "History", "Computer"]

MAX_MARKS = 100

PASS_MARK = 40





def accept_marks(subjects):

    """Ask for marks in each subject and return them as a list."""

    marks = []

    for subject in subjects:

        while True:                       # keep asking until the input is valid

            try:

                value = float(input(f"Enter marks for {subject} (0-{MAX_MARKS}): "))

            except ValueError:

                print("Please enter a valid number.")

                continue

            if 0 <= value <= MAX_MARKS:

                marks.append(value)

                break

            print(f"Marks must be between 0 and {MAX_MARKS}.")

    return marks





def calculate_total(marks):

    """Return the sum of all marks."""

    total = 0

    for mark in marks:

        total += mark

    return total





def calculate_percentage(total, max_total):

    """Return percentage scored."""

    return total / max_total * 100





def assign_grade(percentage):

    """Return a letter grade for the given percentage."""

    if percentage >= 90:

        return "A+"

    if percentage >= 80:

        return "A"

    if percentage >= 70:

        return "B"

    if percentage >= 60:

        return "C"

    if percentage >= 40:

        return "D"

    return "F"





def determine_result(marks):

    """Return PASS only if every subject is at or above the pass mark."""

    for mark in marks:

        if mark < PASS_MARK:

            return "FAIL"

    return "PASS"





def display_result(name, subjects, marks, total, percentage, grade, result):

    """Print the full result card."""

    print("\n" + "=" * 35)

    print(f"Result Card: {name}")

    print("=" * 35)

    for subject, mark in zip(subjects, marks):

        print(f"{subject:<12}: {mark}")

    print("-" * 35)

    print(f"Total      : {total} / {len(subjects) * MAX_MARKS}")

    print(f"Percentage : {percentage:.2f}%")

    print(f"Grade      : {grade}")

    print(f"Result     : {result}")





def main():

    name = input("Enter student name: ").strip() or "Student"

    marks = accept_marks(SUBJECTS)

    total = calculate_total(marks)

    percentage = calculate_percentage(total, len(SUBJECTS) * MAX_MARKS)

    grade = assign_grade(percentage)

    result = determine_result(marks)

    display_result(name, SUBJECTS, marks, total, percentage, grade, result)





if __name__ == "__main__":

    main()
