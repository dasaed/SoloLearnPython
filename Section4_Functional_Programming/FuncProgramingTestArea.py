from math import sqrt
def help():
    """
    Functional Programming is a style of programming that (as the name suggests) is based around functions

    :return:
    """
#This is the first simple example of Functional Programming

def example1(func, arg):
    return func(func(arg))

def add_five(x):
    return (x + 5)
print(example1(add_five, 10))


#lambda functions
def example2(f,arg):
    return f(arg)
print(example2(lambda x: x**2 + 2*x + 1, 3))

print("""
# the following 2 functions do the same thing
  #Normal Function               # Lambda Function
def polynomial(x):              |print((lambda x: x**2 + 5*x + 4)(4))
    return x**2 + 5*x + 4       |
print(polynomial(4))            |
""")


sroot = lambda x: sqrt(x)
print("The Square root of 49 is: "+str(sroot(49)))


print("Maps and Filters")
numbers = [23,52,65,5,8,12,9,2,4,7]

mapResult = list(map(add_five, numbers))
print(mapResult)
filterResult = list(filter(lambda x: x%4 == 0, numbers))
print(filterResult)


#######################################
print("Understanding Generators - yield")
print("The yield function is a little harder to understand, as it doesn't save the values it generates as it \"iterates\"")
def countdown():
    i=0
    while True:
        i+=1
        yield i**2
        if (input("Continue?") == "y"):
            continue
        else:
            return i**2
for y in countdown():
    print(y)


def finitecountdown(i):
    while i>0:
        i-=1
        if i%3 == 0:
            yield i
        else:
            continue

countVal = input("Please input a number: ")
myList = list(finitecountdown(int(countVal)))
print(myList)



















