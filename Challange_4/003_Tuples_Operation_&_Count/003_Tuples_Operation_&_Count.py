# Challenge 3: Tuple Operations & Count
# Program by: Zulfiqar Ahmadi
# Date: March 26, 2025
# Purpose: Count occurrences of a specific value in a tuple

# Creating a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

# User input
fruit_name = input("Enter a fruit name: ").lower()

# Counting occurrences
count = fruit_tuple.count(fruit_name)

print(f"'{fruit_name}' appears {count} times in the tuple.")
