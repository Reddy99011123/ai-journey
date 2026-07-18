name = input("What is your name? ")

print(f"\nHello, {name}!")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

operation = input("\nChoose operation (+ - * /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print("\nResult:", result)