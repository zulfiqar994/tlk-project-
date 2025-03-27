# Challenge 2: Swapping Values Using Tuples
# Program by: Zulfiqar Ahmadi
# Date: March 26, 2025
# Purpose: Swapping values using tuples without a temporary variable

# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Storing in a tuple
numbers = (num1, num2)

# Swapping using tuple unpacking
num1, num2 = num2, num1

print("Swapped Values:", (num1, num2))
