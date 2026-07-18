def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

greet_user()
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."
print("Result:", result)    