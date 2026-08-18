# Calculator with basic operations; User chooses operation and inputs numbers; without exception handling for invalid inputs.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo by zero.")
    return x % y


def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")

    choice = input("Enter choice (1/2/3/4/5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5":
        print(f"{num1} % {num2} = {modulo(num1, num2)}")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
