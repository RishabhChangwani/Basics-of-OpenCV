from calculator import Calculator


def get_number(prompt: str) -> float:
    """
    Prompts the user to enter a number and returns it as a float.
    Handles invalid input by asking the user to enter the number again.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation() -> str:
    """
    Prompts the user to choose an operation and returns the operation as a string.
    """
    operations = {'1': 'add', '2': 'subtract', '3': 'multiply', '4': 'divide'}
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter the number of the operation you want to perform: ")
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice. Please select a valid operation.")


def main():
    """
    Main function to run the calculator application.
    """
    print("Simple Calculator App")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    calculator = Calculator()

    try:
        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)

        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
