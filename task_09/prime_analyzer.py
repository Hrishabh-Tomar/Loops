"""Prime number analyzer for a range.



Sample:

    Start: 10  End: 30

    Primes: [11, 13, 17, 19, 23, 29] | Count: 6 | Sum: 112 | Largest: 29

"""





def is_prime(number):

    """Return True if number is prime."""

    if number < 2:

        return False

    divisor = 2

    while divisor * divisor <= number:    # only need to check up to the square root

        if number % divisor == 0:

            return False

        divisor += 1

    return True





def find_primes(start, end):

    """Return a list of primes between start and end (inclusive)."""

    primes = []

    for number in range(start, end + 1):

        if is_prime(number):

            primes.append(number)

    return primes





def count_primes(primes):

    """Return how many primes are in the list."""

    count = 0

    for _ in primes:

        count += 1

    return count





def sum_primes(primes):

    """Return the sum of the primes."""

    total = 0

    for prime in primes:

        total += prime

    return total





def largest_prime(primes):

    """Return the largest prime, or None if there are none."""

    largest = None

    for prime in primes:

        if largest is None or prime > largest:

            largest = prime

    return largest





def main():

    try:

        start = int(input("Enter start of range: "))

        end = int(input("Enter end of range: "))

    except ValueError:

        print("Please enter whole numbers only.")

        return



    if start > end:

        start, end = end, start

        print(f"Range swapped to {start} - {end}.")



    primes = find_primes(start, end)

    if not primes:

        print("No prime numbers found in this range.")

        return



    print("Primes  :", primes)

    print("Count   :", count_primes(primes))

    print("Sum     :", sum_primes(primes))

    print("Largest :", largest_prime(primes))





if __name__ == "__main__":

    main()
