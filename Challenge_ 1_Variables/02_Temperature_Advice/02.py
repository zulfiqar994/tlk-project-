# Input: Ask user for current temperature in Celsius
temperature = float(input("Enter the temperature: "))

# Conditional statements to provide advice based on temperature
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")