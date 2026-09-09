import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


def floor_division(a, b):
    if b == 0:
        return None
    return a // b

# DISPLAY MENU

def display_menu():
    print("\n" + "=" * 40)
    print("             PYTHON CALCULATOR")
    print("=" * 40)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    print("=" * 55)

# CALCULATOR

def calculator():

    while True:

        display_menu()

        choice = input("Choose an operation: ").strip()

        if choice == "8":
            print("\nCalculator closed successfully.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid operation.")
            continue

        try:

            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(number1, number2)
                symbol = "+"

            elif choice == "2":
                result = subtract(number1, number2)
                symbol = "-"

            elif choice == "3":
                result = multiply(number1, number2)
                symbol = "*"

            elif choice == "4":
                result = divide(number1, number2)
                symbol = "/"

            elif choice == "5":
                result = modulus(number1, number2)
                symbol = "%"

            elif choice == "6":
                result = power(number1, number2)
                symbol = "^"

            elif choice == "7":
                result = floor_division(number1, number2)
                symbol = "//"

            if result is None:
                print("Error: Division by zero is not allowed.")

            else:
                print("\n" + "-" * 55)
                print(f"Calculation : {number1} {symbol} {number2}")
                print(f"Result      : {result}")
                print("-" * 55)

        except ValueError:
            print("Invalid input. Please enter numbers only.")


# ---------------------------------------------------------
# START PROGRAM
# ---------------------------------------------------------
if __name__ == "__main__":
    calculator()