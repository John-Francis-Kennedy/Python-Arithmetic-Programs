# Part 2: Multiplication and Division

# Ask user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
multiplication = num1 * num2

# Display results
print("Multiplication result:", multiplication)

if num2 != 0:
    division = num1 / num2
    print("Division result:", division)
else:
    print("Division by zero is not allowed.")

