def allFunc():
    print("""
    All Functions must follow these rules:
    1. Begin with the keyword def
    2. Be declared before being used 
    """)

def funWithArgs(word):
    print("""
    This functions takes arguments
    """)
    print("This was your word: " + word)

def anotherFun(x,y):
    print(x*2)
    print(y*3)

def func1(x,y):
    if x>y:
        print(str(x)+" is greater")
        return x
    elif x==y:
        print(str(x)+" and "+str(y)+" are the same")
        return "They are equal"
    else:
        print(str(y)+" is greater")
        return y

def funDocStrings():
    """
    DocStrings are comments just below the function that the programmer can access during runtime and error
    checking to see what the function does. It is sort of like the --help option you see with various linux
    commands. To print out the Doc String, you have to execute the following command:
    print(function.__doc__)
    :return:
    """
    print("I hope this was helpful")
def aFunction():
    return "This function only displays this message"

def funcWithinFunc(aFunction, aWord):
    print(aFunction()+aWord)

#the following variable is equal to a function
a = aFunction()

print('anotherFun("two",4)')
anotherFun("two",4)
print('func1(2,4)')
func1(2,4)
print('print(func1("two","three"))')
print(func1("two","three"))
print('print(funDocStrings.__doc__)')
print(funDocStrings.__doc__)
print('funcWithinFunc(hello, "world")')
funcWithinFunc(aFunction, " and this part is created ")
print(a)
