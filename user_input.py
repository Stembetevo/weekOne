num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("+,-,/,*: ")

if operation == "+":
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    if(num2 == 0 or num1 == 0):
        print("Error: Division by zero is not allowed")
    else:
        print("Result: ", num1/num2)
    
    print(num1 / num2)
elif operation == '*':
    print("Result",num1 * num2)