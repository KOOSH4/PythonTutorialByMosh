userInput = input("Enter your name:")
if len(userInput) < 3:
    print("Name must be at least 3 characters.")
elif len(userInput) > 50:
    print("Name can be Maximum of 50 characters.")
else:
    print("Name looks good!")
