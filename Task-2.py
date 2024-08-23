def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The sum of the given numbers are : {add(num1, num2)}")
        elif choice == '2':
            print(f"The difference of the given  numbers are: = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The product of the given numbers are = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The division of the given numbers are = {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
