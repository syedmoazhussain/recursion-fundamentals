def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("Enter a number: "))

print(f"Factorial of {number}: {factorial(number)}")
print("Fibonacci sequence:")
for i in range(number):
    print(fibonacci(i), end=" ")
