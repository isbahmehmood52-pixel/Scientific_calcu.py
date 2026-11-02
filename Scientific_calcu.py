import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error Division by zero."
    return x / y


def square_root(x):
    if x < 0:
        return "Error! Negative number ka square root real numbers mein nahi hota."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm non-positive numbers ke liye defined nahi hai."
    return math.log(x)

def sine(x_deg):

    return math.sine

def cosine(x_deg):
    return math.cosine


def calculator():
    while True:
        print("\n=== SCIENTIFIC CALCULATOR ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power")
        print("7. Logarithm")
        print("8. Sine")
        print("9. Cosine")
        print("11. Exit")
        
        choice = input("Option select karein (1-11): ")

        if choice == '11':
            print("calculator closed")
            break


        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Nuber: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '6':
                print(f"Result: {power(num1, num2)}")


        elif choice in ['5', '7', '8', '9']:
            num = float(input("Enter number: "))

            if choice == '5':
                print(f"Result: {square_root(num)}")
            elif choice == '7':
                print(f"Result: {logarithm(num)}")
            elif choice == '8':
                print(f"Result: {sine(num)}")
            elif choice == '9':
                print(f"Result: {cosine(num)}")
        
        else:
            print("Invalid input Please select number between 1 to 11.")

calculator()