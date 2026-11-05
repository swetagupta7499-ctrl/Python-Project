
LOG_FILE = "toolkit_results.txt"

session_data = {
    "group": "Group 8",
    "members": ["Rajesh Chaurasiya", "Manas Dubey", "Sweta", "Pavan Kumar"],
    "primes_found": set(),
    "history": []
}


# 1. NUMBER CHECKS

def is_prime(n):
    """
    Check whether a number is prime.

    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    """
    Check whether a number is palindrome.

    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    """
    s = str(abs(n))

    if s == s[::-1]:
        return True
    else:
        return False


def is_armstrong(n):
    """
    Check whether a number is Armstrong.

    >>> is_armstrong(153)
    True
    >>> is_armstrong(123)
    False
    """
    if n < 0:
        return False

    s = str(n)
    power = len(s)
    total = 0

    for digit in s:
        total += int(digit) ** power

    return total == n


def is_perfect(n):
    """
    Check whether a number is perfect.

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
    Return prime, palindrome, Armstrong and perfect results.

    >>> check_number_properties(6)
    (False, True, True, True)
    >>> check_number_properties(7)
    (True, True, True, False)
    """
    prime = is_prime(n)

    if prime:
        session_data["primes_found"].add(n)

    pal = is_palindrome(n)
    arm = is_armstrong(n)
    perf = is_perfect(n)

    return (prime, pal, arm, perf)


# 2. DIGIT OPERATIONS

def digit_operations(n):
    """
    Find sum, count and reverse of digits.

    >>> digit_operations(1234)
    (10, 4, 4321)
    >>> digit_operations(508)
    (13, 3, 805)
    """
    temp = abs(n)

    total = 0
    count = 0
    rev = 0

    if temp == 0:
        return (0, 1, 0)

    while temp > 0:
        digit = temp % 10

        total += digit
        count += 1
        rev = rev * 10 + digit

        temp = temp // 10

    if n < 0:
        rev = -rev

    return (total, count, rev)


# 3. RECURSION

def factorial_recursive(n):
    """
    Calculate factorial using recursion.

    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(0)
    1
    """
    if n < 0:
        raise ValueError("Enter a positive number")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Find nth Fibonacci number.

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
    Generate Fibonacci series.

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
    Calculate GCD using recursion.

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
    Find GCD and LCM.

    >>> gcd_and_lcm(12, 18)
    (6, 36)
    >>> gcd_and_lcm(7, 5)
    (1, 35)
    """
    g = gcd_recursive(a, b)

    if a == 0 or b == 0:
        return (g, 0)

    lcm = abs(a * b) // g

    return (g, lcm)


# 4. NESTED LOOPS

def primes_up_to_n(n):
    """
    Find all prime numbers up to N.

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
    Generate multiplication tables.

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


# 5. FILE HANDLING

def save_result_to_file(operation, input_val, result, filename=LOG_FILE):
    """
    Save results in a file.

    >>> save_result_to_file("Test", 5, "Success", "test_log.txt")
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

    with open(filename, "a") as file:
        file.write(str(record) + "\n")

    return True


# 6. INTERACTIVE MENU

print("PROJECT 8: NUMBER UTILITY TOOLKIT")
print("Group:", session_data["group"])
print("Members:", session_data["members"])

while True:

    print("\n1. Check Number Properties")
    print("2. Digit Operations")
    print("3. Fibonacci and Factorial")
    print("4. GCD and LCM")
    print("5. Prime Numbers up to N")
    print("6. Multiplication Tables")
    print("7. View Session Data")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            n = int(input("Enter number: "))

            result = check_number_properties(n)

            print("Prime, Palindrome, Armstrong, Perfect:")
            print(result)

            save_result_to_file("Number Check", n, result)

        elif choice == "2":
            n = int(input("Enter number: "))

            result = digit_operations(n)

            print("Sum, Count, Reverse:", result)

            save_result_to_file("Digit Operations", n, result)

        elif choice == "3":
            n = int(input("Enter number: "))

            fib = get_fibonacci_series(n)
            fact = factorial_recursive(n)

            print("Fibonacci:", fib)
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
            start = int(input("Starting number: "))
            end = int(input("Ending number: "))

            if start > end:
                start, end = end, start

            lines = generate_multiplication_tables(start, end)

            count = 0

            for line in lines:
                print(line)

                count += 1

                if count % 10 == 0:
                    print("--------------------")

            save_result_to_file("Tables", (start, end), "Completed")

        elif choice == "7":
            print("Group:", session_data["group"])
            print("Primes Found:", session_data["primes_found"])
            print("History:", session_data["history"])

        elif choice == "8":
            print("All results saved. Goodbye!")
            break

        else:
            print("Invalid choice")

    except ValueError as e:
        print("Error:", e)

    except RecursionError:
        print("Number is too large")

    except IOError:
        print("File could not be saved")
