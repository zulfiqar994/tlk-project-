# Input: Ask user for the current day of the week
day = input("Enter the day of the week: ").capitalize()

# Conditional statements to suggest an activity based on the day
if day == "Monday":
    print("Start your week with a workout!")
elif day == "Tuesday":
    print("It's a great day to read a book!")
elif day == "Wednesday":
    print("Mid-week movie night!")
elif day == "Thursday":
    print("Try a new recipe!")
elif day == "Friday":
    print("Relax and enjoy the weekend!")
elif day == "Saturday":
    print("Go for a hike!")
elif day == "Sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("Invalid day. Please enter a valid day of the week.")
