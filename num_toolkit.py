# PROJECT 8: NUMBER UTILITY TOOLKIT
# Group 8: Rajesh Chaurasiya, Manas Dubey, Sweta, Pavan Kumar

# Session data
primes = []
history = []


# Check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Check palindrome
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# Check Armstrong
def is_armstrong(n):
    s = str(n)
    total = 0
    for d in s:
        total = total + int(d) ** len(s)
    return total == n


# Check perfect number
def is_perfect(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total == n


# Sum, count and reverse of digits
def digit_ops(n):
    total = 0
    count = 0
    rev = 0
    while n > 0:
        d = n % 10
        total = total + d
        count = count + 1
        rev = rev * 10 + d
        n = n // 10
    return total, count, rev


# Factorial (recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci number (recursion)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# GCD (recursion)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Fibonacci series
def fib_series(terms):
    series = []
    for i in range(terms):
        series.append(fib(i))
    return series


# Prime numbers up to N
def primes_upto(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
            if i not in primes:
                primes.append(i)
    return result


# Multiplication tables
def print_tables(start, end):
    for num in range(start, end + 1):
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
        print("--------------------")


# Save result in file
def save(operation, inp, result):
    text = operation + " | Input: " + str(inp) + " | Result: " + str(result)
    history.append(text)
    f = open("results.txt", "a")
    f.write(text + "\n")
    f.close()


# Main program
print("PROJECT 8: NUMBER UTILITY TOOLKIT")
print("Group 8: Rajesh Chaurasiya, Manas Dubey, Sweta, Pavan Kumar")

while True:
    # Menu
    print("\n--- MAIN MENU ---")
    print("1. Check Prime, Palindrome, Armstrong, Perfect")
    print("2. Sum, Count and Reverse of Digits")
    print("3. Fibonacci Series and Factorial")
    print("4. GCD and LCM")
    print("5. Prime Numbers up to N")
    print("6. Multiplication Tables")
    print("7. View Session Data")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    try:
        # Option 1: Number checks
        if choice == "1":
            n = int(input("Enter a positive integer: "))
            p = is_prime(n)
            result = (p, is_palindrome(n), is_armstrong(n), is_perfect(n))
            if p and n not in primes:
                primes.append(n)
            print("Prime, Palindrome, Armstrong, Perfect:", result)
            save("Number Check", n, result)

        # Option 2: Digit operations
        elif choice == "2":
            n = int(input("Enter a positive integer: "))
            result = digit_ops(n)
            print("Sum, Count, Reverse:", result)
            save("Digit Operations", n, result)

        # Option 3: Fibonacci and factorial
        elif choice == "3":
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Number must not be negative.")
            else:
                series = fib_series(n)
                fact = factorial(n)
                print("Fibonacci Series:", series)
                print("Factorial:", fact)
                save("Fibonacci and Factorial", n, (series, fact))

        # Option 4: GCD and LCM
        elif choice == "4":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            g = gcd(a, b)
            lcm = a * b // g
            print("GCD:", g)
            print("LCM:", lcm)
            save("GCD and LCM", (a, b), (g, lcm))

        # Option 5: Primes up to N
        elif choice == "5":
            n = int(input("Enter N: "))
            result = primes_upto(n)
            print("Prime Numbers:", result)
            save("Prime Numbers", n, result)

        # Option 6: Multiplication tables
        elif choice == "6":
            start = int(input("Enter starting number: "))
            end = int(input("Enter ending number: "))
            print_tables(start, end)
            save("Multiplication Tables", (start, end), "Done")

        # Option 7: Session data
        elif choice == "7":
            print("Primes Found:", primes)
            print("Total Runs:", len(history))
            for h in history:
                print(h)

        # Option 8: Exit
        elif choice == "8":
            print("All results are saved in results.txt")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Select 1 to 8.")

    # Error handling
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("GCD is 0, so LCM cannot be found.")
