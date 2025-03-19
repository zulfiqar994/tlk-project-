# Sum of Numbers
# Purpose: This script calculates the sum of all numbers from 1 to a user-entered number using a for loop.
# Author: Zulfiqar
# Date: 2025-03_Even_or_Odd_Number_Checker Skipping Even Numbers-13

# Get user input and convert to integer
n = int(input("Enter a number: "))

# Initialize sum variable
sum_numbers = 0

# Loop to calculate sum
for num in range(1, n + 1):
    sum_numbers += num

# Print the result
print("Sum =", sum_numbers)

