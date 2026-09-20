"""Employee salary analyzer.



Sample output:

    Total payroll: 285000 | Average: 57000.00

    Highest: Ravi (90000) | Lowest: Meena (30000)

    Above average: Ravi, Asha

"""



EMPLOYEES = {

    "Asha": 60000,

    "Ravi": 90000,

    "Meena": 30000,

    "Kiran": 45000,

    "Sara": 60000,

}





def total_payroll(salaries):

    """Return the sum of all salaries."""

    total = 0

    for salary in salaries.values():

        total += salary

    return total





def average_salary(salaries):

    """Return the mean salary."""

    if not salaries:

        raise ValueError("No employees given.")

    return total_payroll(salaries) / len(salaries)





def highest_salary(salaries):

    """Return (name, salary) of the top earner."""

    top_name, top_salary = None, None

    for name, salary in salaries.items():

        if top_salary is None or salary > top_salary:

            top_name, top_salary = name, salary

    return top_name, top_salary





def lowest_salary(salaries):

    """Return (name, salary) of the lowest earner."""

    low_name, low_salary = None, None

    for name, salary in salaries.items():

        if low_salary is None or salary < low_salary:

            low_name, low_salary = name, salary

    return low_name, low_salary





def above_average(salaries):

    """Return names of employees earning more than the average."""

    average = average_salary(salaries)

    return [name for name, salary in salaries.items() if salary > average]





def main():

    try:

        print(f"Total payroll  : {total_payroll(EMPLOYEES)}")

        print(f"Average salary : {average_salary(EMPLOYEES):.2f}")

        name, salary = highest_salary(EMPLOYEES)

        print(f"Highest salary : {name} ({salary})")

        name, salary = lowest_salary(EMPLOYEES)

        print(f"Lowest salary  : {name} ({salary})")

        print("Above average  :", ", ".join(above_average(EMPLOYEES)))

    except ValueError as error:

        print("Error:", error)





if __name__ == "__main__":

    main()
