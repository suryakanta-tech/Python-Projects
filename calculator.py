''' in this project we create a simple calculator usng python. '''

num1 = int(input("Enter your first number: "))
operator = input("Enter your operator(+,-,*,/,%,**): ")
num2 = int(input("Enter your second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    result = "Error! Enter a valid operator."

print(f"Result: {num1} {operator} {num2} = {result}")