def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        result = num1 + num2
        print(f"The result is: {num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"The result is: {num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"The result is: {num1} * {num2} = {result}")
    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            result = num1 / num2
            print(f"The result is: {num1} / {num2} = {result}")
    elif choice == 5:
        print("Exiting the calculator...")
        print("Exited...")
        
        return

if __name__ == "__main__":
    calculator()
