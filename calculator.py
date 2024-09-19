# Function to perform the calculation
def calculator():
    # Prompt user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user to select an operation
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform calculation based on operation
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

# Call the calculator function
calculator()
