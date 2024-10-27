# calculator python

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

# operator
operator = input("Pick operator (+ - / * % **): ")

while True:

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '**':
        result = num1 ** num2
    else:
        print("Invalid operator! : ")
        
    print(result)
    