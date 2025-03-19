
count = 10
while count > 0:
    print(count)
    user_input = input("Enter 'stop' to cancel or press Enter: ")
    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break
    count -= 1



