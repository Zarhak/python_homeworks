def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = sub(num1, num2)
elif op == "*":
    result = mult(num1, num2)
elif op == "/":
    result = div(num1, num2)
else:
    result = "Invalid operation"

print(f"Result: {result}")