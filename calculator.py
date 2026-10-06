# Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Take input from the user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid operator. Please use +, -, * or /.")

except ValueError:
    print("Invalid input. Please enter numbers only.")