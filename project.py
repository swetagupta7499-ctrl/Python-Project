LOG_FILE = "toolkit_results.txt"

session_data = {
    "group": "Group 8",
    "members": ["Rajesh Chaurasiya", "Manas Dubey", "Sweta", "Pavan Kumar"],
    "primes_found": set(),
    "history": []
}


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    """
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    """
    s = str(abs(n))
    return s == s[::-1]


def is_armstrong(n):
    """
    >>> is_armstrong(153)
    True
    >>> is_armstrong(123)
    False
    """
    if n < 0:
        return False

    s = str(n)
    total = 0

    for digit in s:
        total += int(digit) ** len(s)

    return total == n


def is_perfect(n):
    """
    >>> is_perfect(6)
    True
    >>> is_perfect(10)
    False
    """
    if n < 2:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


def check_number_properties(n):
    """
    >>> check_number_properties(6)
    (False, True, True, True)
    >>> check_number_properties(7)
    (True, True, True, False)
    """
    prime = is_prime(n)
    palindrome = is_palindrome(n)
    armstrong = is_armstrong(n)
    perfect = is_perfect(n)

    if prime:
        session_data["primes_found"].add(n)

    return prime, palindrome, armstrong, perfect


def digit_operations(n):
    """
    >>> digit_operations(1234)
    (10, 4, 4321)
    >>> digit_operations(508)
    (13, 3, 805)
    """
    temp = abs(n)
    total = 0
    count = 0
    reverse = 0

    if temp == 0:
        return 0, 1, 0

    while temp > 0:
        digit = temp % 10

        total += digit
        count += 1
        reverse = reverse * 10 + digit

        temp = temp // 10

    if n < 0:
        reverse = -reverse

    return total, count, reverse


def factorial_recursive(n):
    """
    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(0)
    1
    """
    if n < 0:
        raise ValueError("Enter a non-negative number")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    >>> fibonacci_recursive(0)
    0
    >>> fibonacci_recursive(6)
    8
    """
    if n < 0:
        raise ValueError("Enter a non-negative number")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def get_fibonacci_series(terms):
    """
    >>> get_fibonacci_series(5)
    [0, 1, 1, 2, 3]
    >>> get_fibonacci_series(1)
    [0]
    """
    if terms < 0:
        raise ValueError("Enter a non-negative number")

    series = []

    for i in range(terms):
        series.append(fibonacci_recursive(i))

    return series


def gcd_recursive(a, b):
    """
    >>> gcd_recursive(48, 18)
    6
    >>> gcd_recursive(15, 25)
    5
    """
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd_recursive(b, a % b)


def gcd_and_lcm(a, b):
    """
    >>> gcd_and_lcm(12, 18)
    (6, 36)
    >>> gcd_and_lcm(7, 5)
    (1, 35)
    """
    g = gcd_recursive(a, b)

    if a == 0 or b == 0:
        return g, 0

    lcm = abs(a * b) // g

    return g, lcm


def primes_up_to_n(n):
    """
    >>> primes_up_to_n(10)
    [2, 3, 5, 7]
    >>> primes_up_to_n(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    primes = set()

    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            primes.add(num)
            session_data["primes_found"].add(num)

    return sorted(primes)


def generate_multiplication_tables(start, end):
    """
    >>> len(generate_multiplication_tables(2, 3))
    20
    >>> generate_multiplication_tables(2, 2)[0]
    '2 x 1 = 2'
    """
    lines = []

    for num in range(start, end + 1):
        for i in range(1, 11):
            lines.append(f"{num} x {i} = {num * i}")

    return lines


def save_result_to_file(operation, input_val, result):
    """
    >>> save_result_to_file("Test", 5, "Success")
    True
    """
    run = len(session_data["history"]) + 1

    record = {
        "run": run,
        "operation": operation,
        "input": input_val,
        "result": result
    }

    session_data["history"].append(record)

    file = open(LOG_FILE, "a")
    file.write(str(record) + "\n")
    file.close()

    return True


print("=" * 50)
print("PROJECT 8: NUMBER UTILITY TOOLKIT")
print("Group:", session_data["group"])
print("Members:", ", ".join(session_data["members"]))
print("=" * 50)


while True:

    print("\n--- MAIN MENU ---")
    print("1. Check Prime, Palindrome, Armstrong or Perfect")
    print("2. Sum, Count and Reverse of Digits")
    print("3. Fibonacci Series and Factorial")
    print("4. GCD and LCM")
    print("5. Prime Numbers up to N")
    print("6. Multiplication Tables")
    print("7. View Session Data")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    try:

        if choice == "1":
            n = int(input("Enter an integer: "))

            result = check_number_properties(n)

            print("Prime, Palindrome, Armstrong, Perfect:")
            print(result)

            save_result_to_file("Number Check", n, result)

        elif choice == "2":
            n = int(input("Enter an integer: "))

            result = digit_operations(n)

            print("Sum, Count, Reverse:", result)

            save_result_to_file("Digit Operations", n, result)

        elif choice == "3":
            n = int(input("Enter a non-negative integer: "))

            fib = get_fibonacci_series(n)
            fact = factorial_recursive(n)

            print("Fibonacci Series:", fib)
            print("Factorial:", fact)

            save_result_to_file("Fibonacci and Factorial", n, (fib, fact))

        elif choice == "4":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            result = gcd_and_lcm(a, b)

            print("GCD and LCM:", result)

            save_result_to_file("GCD and LCM", (a, b), result)

        elif choice == "5":
            n = int(input("Enter N: "))

            result = primes_up_to_n(n)

            print("Prime Numbers:", result)

            save_result_to_file("Prime Numbers", n, result)

        elif choice == "6":
            start = int(input("Enter starting number: "))
            end = int(input("Enter ending number: "))

            if start > end:
                start, end = end, start

            lines = generate_multiplication_tables(start, end)

            count = 0

            for line in lines:
                print(line)
                count += 1

                if count % 10 == 0:
                    print("--------------------")

            save_result_to_file("Multiplication Tables", (start, end), "Completed")

        elif choice == "7":
            print("\n--- SESSION DATA ---")
            print("Group:", session_data["group"])
            print("Primes Found:", session_data["primes_found"])
            print("Total Runs:", len(session_data["history"]))

            for entry in session_data["history"]:
                print(entry)

        elif choice == "8":
            print("All results saved to", LOG_FILE)
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Select 1 to 8.")

    except ValueError as e:
        print("Input Error:", e)

    except RecursionError:
        print("Number is too large.")

    except IOError:
        print("File could not be saved.")
