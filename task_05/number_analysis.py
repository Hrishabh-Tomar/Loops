"""Number analysis without min(), max() or sum().



Sample:

    Input : 4 -7 12 0 9 -2

    Output: largest=12, smallest=-7, total=16, average=2.67,

            even=3, odd=2, positive=3, negative=2

"""





def analyze_numbers(numbers):

    """Return a dict of statistics for a non-empty list of integers."""

    if not numbers:

        raise ValueError("The list is empty.")



    largest = numbers[0]

    smallest = numbers[0]

    total = 0

    count = 0

    even_count = odd_count = positive_count = negative_count = 0



    for number in numbers:

        if number > largest:

            largest = number

        if number < smallest:

            smallest = number

        total += number

        count += 1



        if number % 2 == 0:

            even_count += 1

        else:

            odd_count += 1



        if number > 0:

            positive_count += 1

        elif number < 0:

            negative_count += 1           # zero is neither positive nor negative



    return {

        "largest": largest,

        "smallest": smallest,

        "total": total,

        "average": total / count,

        "even count": even_count,

        "odd count": odd_count,

        "positive count": positive_count,

        "negative count": negative_count,

    }





def main():

    raw = input("Enter integers separated by spaces: ").split()

    try:

        numbers = [int(item) for item in raw]

        results = analyze_numbers(numbers)

    except ValueError as error:

        print("Error:", error if str(error) == "The list is empty." else "Please enter integers only.")

        return



    for label, value in results.items():

        if label == "average":

            print(f"{label.capitalize():<15}: {value:.2f}")

        else:

            print(f"{label.capitalize():<15}: {value}")





if __name__ == "__main__":

    main()
