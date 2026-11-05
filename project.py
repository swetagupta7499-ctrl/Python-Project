

LOG_FILE = "toolkit_results.txt"


# ==============================================================================
# 1. NUMBER CHECKS (Prime, Palindrome, Armstrong, Perfect Number)
# ==============================================================================

def is_prime(n):
    """
    Check if a number is prime.
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
    Check if a number is a palindrome using string manipulation.
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    """
    s = str(abs(n))
    return s == s[::-1]


def is_armstrong(n):
    """
    Check if a number is an Armstrong number.
    >>> is_armstrong(153)
    True
    >>> is_armstrong(370)
    True
    >>> is_armstrong(123)
    False
    """
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def is_perfect(n):
    """
    Check if a number is a perfect number.
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(10)
    False
    """
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return divisors_sum == n


def check_number_properties(n):
    """
    Return all 4 property checks as a tuple (Prime, Palindrome, Armstrong, Perfect).
    >>> check_number_properties(6)
    (False, True, True, True)
    >>> check_number_properties(7)
    (True, True, True, False)
    """
    prime = is_prime(n)
    if prime:
        session_data["primes_found"].add(n)
    return (prime, is_palindrome(n), is_armstrong(n), is_perfect(n))


# ==============================================================================
# 2. DIGIT OPERATIONS (Sum, Count, and Reverse - Returned as a Tuple)
# ==============================================================================

def digit_operations(n):
    """
    Find the sum of digits, count of digits, and reverse of a number.
    Returns a tuple: (sum_of_digits, count_of_digits, reversed_number).
    >>> digit_operations(1234)
    (10, 4, 4321)
    >>> digit_operations(508)
    (13, 3, 805)
    """
    temp = abs(n)
    if temp == 0:
        return (0, 1, 0)
    
    digit_sum = 0
    digit_count = 0
    reversed_num = 0
    
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_count += 1
        reversed_num = (reversed_num * 10) + digit
        temp //= 10
        
    if n < 0:
        reversed_num = -reversed_num
        
    return (digit_sum, digit_count, reversed_num)


# ==============================================================================
# 3. RECURSION TOOLS (Factorial, Fibonacci, and GCD/LCM)
# ==============================================================================

def factorial_recursive(n):
    """
    Compute the factorial of a non-negative integer recursively.
    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(0)
    1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number recursively (0-indexed).
    >>> fibonacci_recursive(0)
    0
    >>> fibonacci_recursive(1)
    1
    >>> fibonacci_recursive(6)
    8
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def get_fibonacci_series(terms):
    """
    Generate a list of Fibonacci series up to 'terms' count.
    >>> get_fibonacci_series(5)
    [0, 1, 1, 2, 3]
    >>> get_fibonacci_series(1)
    [0]
    """
    return [fibonacci_recursive(i) for i in range(terms)]


def gcd_recursive(a, b):
    """
    Find the Greatest Common Divisor (GCD) of two numbers using recursion.
    >>> gcd_recursive(48, 18)
    6
    >>> gcd_recursive(15, 25)
    5
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_and_lcm(a, b):
    """
    Find both GCD and LCM of two numbers and return as a tuple (GCD, LCM).
    >>> gcd_and_lcm(12, 18)
    (6, 36)
    >>> gcd_and_lcm(7, 5)
    (1, 35)
    """
    if a == 0 or b == 0:
        return (max(abs(a), abs(b)), 0)
    g = gcd_recursive(a, b)
    lcm = abs(a * b) // g
    return (g, lcm)


# ==============================================================================
# 4. NESTED LOOPS (Primes up to N & Multiplication Tables)
# ==============================================================================

def primes_up_to_n(n):
    """
    List all prime numbers up to N using nested loops and return as a sorted list.
    Also updates the global set of prime numbers found.
    >>> primes_up_to_n(10)
    [2, 3, 5, 7]
    >>> primes_up_to_n(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    primes_set = set()
    for num in range(2, n + 1):
        is_p = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_p = False
                break
        if is_p:
            primes_set.add(num)
            session_data["primes_found"].add(num)
    return sorted(list(primes_set))


def generate_multiplication_tables(start, end):
    """
    Generate multiplication tables from 'start' to 'end' using nested loops.
    Returns a list of formatted strings for each table row.
    >>> len(generate_multiplication_tables(2, 3))
    20
    >>> generate_multiplication_tables(2, 2)[0]
    '2 x 1 = 2'
    """
    table_lines = []
    for num in range(start, end + 1):
        for mult in range(1, 11):
            table_lines.append(f"{num} x {mult} = {num * mult}")
    return table_lines


# ==============================================================================
# 5. FILE HANDLING & LOGGING (Without any imports)
# ==============================================================================

def save_result_to_file(operation_name, input_val, result_val, filename=LOG_FILE):
    """
    Save the result of every run to a file and record it in the main dictionary.
    >>> save_result_to_file("TestOp", 5, "Success", "test_log.txt")
    True
    """
    run_number = len(session_data["history"]) + 1
    record = {
        "run": run_number,
        "operation": operation_name,
        "input": input_val,
        "result": result_val
    }
    session_data["history"].append(record)
    
    log_entry = f"[Run #{run_number}] Operation: {operation_name} | Input: {input_val} | Result: {result_val}\n"
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(log_entry)
        return True
    except IOError as e:
        print(f"File error: {e}")
        return False


# ==============================================================================
# 6. INTERACTIVE MENU & EXCEPTION HANDLING
# ==============================================================================

def main_menu():
    """Run the interactive Number Utility Toolkit menu."""
    print("=" * 60)
    print("         PROJECT 8: NUMBER UTILITY TOOLKIT")
    print(f"  Group: {session_data['group']} | Members: {', '.join(session_data['members'])}")
    print("=" * 60)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Prime, Palindrome, Armstrong, or Perfect Number")
        print("2. Find Sum of Digits, Count of Digits, and Reverse")
        print("3. Print Fibonacci Series and Factorial (Recursive)")
        print("4. Find GCD and LCM of Two Numbers (Recursive)")
        print("5. List All Prime Numbers up to N (Nested Loops & Sets)")
        print("6. Print Multiplication Tables (Nested Loops)")
        print("7. View Session Data Dictionary & Primes Set")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        try:
            if choice == '1':
                n = int(input("Enter an integer: "))
                prime, pal, arm, perf = check_number_properties(n)
                res_str = f"Prime: {prime}, Palindrome: {pal}, Armstrong: {arm}, Perfect: {perf}"
                print(f"Results for {n} -> {res_str}")
                save_result_to_file("Number Property Check", n, (prime, pal, arm, perf))

            elif choice == '2':
                n = int(input("Enter an integer: "))
                d_sum, d_count, rev = digit_operations(n)
                print(f"Results (Tuple): {(d_sum, d_count, rev)}")
                print(f" -> Sum of Digits: {d_sum} | Count of Digits: {d_count} | Reverse: {rev}")
                save_result_to_file("Digit Operations", n, (d_sum, d_count, rev))

            elif choice == '3':
                n = int(input("Enter a non-negative integer (e.g., 5): "))
                if n < 0:
                    raise ValueError("Please enter a non-negative integer.")
                fib_list = get_fibonacci_series(n)
                fact = factorial_recursive(n)
                result_tuple = (fib_list, fact)
                print(f"Fibonacci Series ({n} terms): {fib_list}")
                print(f"Factorial of {n}: {fact}")
                save_result_to_file("Fibonacci & Factorial", n, result_tuple)

            elif choice == '4':
                a = int(input("Enter first integer: "))
                b = int(input("Enter second integer: "))
                g, l = gcd_and_lcm(a, b)
                print(f"Results (Tuple) -> (GCD, LCM): {(g, l)}")
                save_result_to_file("GCD and LCM", (a, b), (g, l))

            elif choice == '5':
                n = int(input("Find all prime numbers up to N. Enter N: "))
                primes = primes_up_to_n(n)
                print(f"Primes up to {n}: {primes}")
                print(f"All Primes Found in Session Set: {session_data['primes_found']}")
                save_result_to_file("Primes Up to N", n, primes)

            elif choice == '6':
                start = int(input("Enter starting table number: "))
                end = int(input("Enter ending table number: "))
                if start > end:
                    start, end = end, start
                lines = generate_multiplication_tables(start, end)
                print("\n--- Multiplication Tables ---")
                for i, line in enumerate(lines, 1):
                    print(line)
                    if i % 10 == 0:
                        print("-" * 20)
                save_result_to_file("Multiplication Tables", (start, end), f"Generated {len(lines)} rows")

            elif choice == '7':
                print("\n--- SESSION DATA (DICTIONARY & SET) ---")
                print(f"Group: {session_data['group']}")
                print(f"Primes Found Set: {session_data['primes_found']}")
                print(f"Total Runs Logged: {len(session_data['history'])}")
                for entry in session_data['history']:
                    print(f"  [Run #{entry['run']}] {entry['operation']} ({entry['input']}) -> {entry['result']}")

            elif choice == '8':
                print(f"All results saved to '{LOG_FILE}'. Goodbye!")
                break

            else:
                print("Invalid choice! Please select an option from 1 to 8.")

        except ValueError as ve:
            print(f"Input Error: {ve}. Please enter valid integers.")
        except RecursionError:
            print("Error: Number is too large for recursion limit. Please try a smaller number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main_menu()

