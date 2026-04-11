try:
    age = int(input("Enter your age : "))

    if age <= 0 or age > 120:
        print("Enter a realistic age")
    else:
        print("Age is valid")

        if age % 2 == 0:
            print("The age is even")
        else:
            print("The age is odd")

except ValueError:
    print("Please enter a valid number")
