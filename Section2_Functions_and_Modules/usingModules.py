#Importing libraries
import random  #Library that gives you random numbers, and other random related functions
from math import sqrt as squareroot    #Math library, that extends the basic math functionality of Python
from math import pi

def ayuda():
    """
    Modules are pieces of code that other people have written to fulfill common tasks, such as
    generating random numbers, performing mathematical operations, etc.
    Modules are basically libraries and to use, you just import them.
    For example:
    import random
    :return:
    """
    print(ayuda.__doc__)

print("Printint random numbers from 0 to 10")
for i in range(5):
    value =  random.randint(0,11)
    print(value)


print("The square root of PI is: " + str(squareroot(pi)))

def pascLine(depth):
    if depth <=1:
        return [1]
    elif depth > 1:
        line = [1]
        prevLine = pascLine(depth - 1)
        for i in range(len(prevLine) - 1):
            line.append( prevLine[i] + prevLine[i + 1])
        line.append(1)
        return line
    else:
        print("Input needs to be an integer")
        return "Input needs to be an integer"


#def pascTriangle(depth):
#    counter=0
#    triangle=[[1]]
#    while counter < depth:
#        triangle[counter].append(pascLine(counter))
#        counter +=1
#    return triangle
#pascTriangle(2)




