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

print("###############################################################")
print("decorators")

def decor(func):
    def wrap():
        print("###############################################################")
        func()
        print("###############################################################")
    return wrap   

def moredecor(func):
    def mwrap():
        print("**************************************************************")
        func()
        print("**************************************************************")
    return mwrap   


def print_text():
    return "I am just a line"

decorated = decor(  print_text ) 
decorated()

#This is another way of using decorator functions
print("--------------------------------------------------------------")
@moredecor
@decor
@moredecor
def print_mtext():
    print("I am just another line")
print_mtext()

print("--------------------------------------------------------------")
print("######## Sample Basic Recursive Functions ##########")

def recursiveFactorial(x):
    if x<=1:
         return 1
    else:
         return x*recursiveFactorial(x - 1)

print( "The Factorial of 10 is: "+str(recursiveFactorial(10)))



series=[0,1]
def fib(x):
    if x <= 1: 
        return 
    else: 
        series.append(series[len(series) - 2]+series[len(series)-1])
        fib(x-1)
    return series

print( "This is just the output of a fibonacci series up to the 10th term: "+str(fib(10)))

print("########## sets  ##########")
print("""
Sets are the same thing as lists, except their elements cannot be repeated(they are not indexed), and to add or remove elements, you use the methods
.add() and .pop(). In list you would use .apend() or .remove().
Friendly Reminder:
[ ] = list
( ) = tuple
{ } = set
{ } = dictionary ( remember it is with key : value pair)

Also, 

{} = empty dictionary
set() = empty set


Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either. 
The intersection operator & gets items only in both. 
The difference operator - gets items in the first set but not in the second. 
The symmetric difference operator ^ gets items in either set, but not both.
""")

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # prints items in neither
print(first & second) # prints itmes in both
print(first - second) # prints items only in the first, but not the second
print(second - first) # prints itmes only in the second, but not in the first
print(first ^ second) # prints items in either first or second

#    itertools
#    
#    The module itertools is a standard library that contains several functions that are useful in functional programming. 
#    One type of function it produces is infinite iterators. 
#    The function count counts up infinitely from a value. 
#    The function cycle infinitely iterates through an iterable (for instance a list or string). 
#    The function repeat repeats an object, either infinitely or a specific number of times.
#    Example:
#    from itertools import count
#    
#    for i in count(3):
#      print(i)
#      if i >=11:
#        break
#    Try It Yourself
#    
#    Result:
#    >>>
#    3
#    4
#    5
#    6
#    7
#    8
#    9
#    10
#    11
#    >>>
#    There are also several combinatoric functions in itertool, such as 'product' and 'permutation'.
a={1, 2}
print(len(list(product(range(3), a))))

nums = [1, 2, 8, 3, 7]
res = list( filter ( lambda x: x% 2 ==0, nums)) 
print(res) 
