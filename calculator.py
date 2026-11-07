num = float(input("Enter first number: "))

while True:
    op = input("Enter operator (+, -, *, /) or = to finish: ")

    if op == "=":
        print("Result:", num)
        break

    num2 = float(input("Enter next number: "))

    if op == "+":
        num = num + num2
    elif op == "-":
        num = num - num2
    elif op == "*":
        num = num * num2
    elif op == "/":
        num = num / num2
    else:
        print("Invalid operator")