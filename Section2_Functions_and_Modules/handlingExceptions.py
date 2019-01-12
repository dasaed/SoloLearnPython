try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Calculation Done")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

try:
    variable=10
    print(variable + "hello")
    print(variable/2)
except ZeroDivisionError:
    print("You are trying a division by 0")
except (ValueError,TypeError):
    print("an error occured")

