count = 0
a = True
while (a == True):
    print("""
    Options
    Enter 'add' to add 2 numbers
    Enter 'sub' to sub 2 numbers
    Enter 'mul' to multiply 2 numbers
    Enter 'div' to divide 2 numbers
    Enter 'q' to quit
    """)
    operation = input("Please select an option")
    if (operation == "add"):
        print("")
        num1 = input("Number 1")
        num2 = input("Number 2")
        print(str(num1)+"+"+str(num2)+"= "+str(float(num1)+float(num2)))
    elif (operation == "sub"):
        print("")
        num1 = input("Number 1")
        num2 = input("Number 2")
        print(str(num1)+"-"+str(num2)+"= "+str(float(num1)-float(num2)))
    elif (operation == "mul"):
        print("")
        num1 = input("Number 1")
        num2 = input("Number 2")
        print(str(num1)+"*"+str(num2)+"= "+str(float(num1)*float(num2)))
    elif (operation == "div"):
        print("")
        num1 = input("Number 1")
        num2 = input("Number 2")
        print(str(num1) + "*" + str(num2) + "= " + str(float(num1)/float(num2)))
    elif (operation == "q"):
        a=False
    else:
        print("Please select a valid option")


