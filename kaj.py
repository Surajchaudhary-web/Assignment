print("Simple Calculator")
print("-----------------")

while True:
    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Operator input
    opr = input("Enter operator (+, -, *, /): ")

    # Using if-else to calculate
    if opr == "+":
        print("Result =", num1 + num2)
    elif opr == "-":
        print("Result =", num1 - num2)
    elif opr == "*":
        print("Result =", num1 * num2)
    elif opr == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operator!")

    # Asking if user wants to continue
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for using the calculator! 👋")
        break
