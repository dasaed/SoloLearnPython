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
except:
    print("any other error would actually be caught here")
finally:
    print("any code in a finally will always run, always")

print("You can also raise your own errors. In other words, code exceptions that might happen, so that if someone writes something the code isn't supposed to do, you will manually alert the user of such error")

###
#var1 = 10
#var2 = "HELLO WORLD"
#if isinstance(var2,str):
#    raise TypeError("var 2 nees to be an integer")

#try:
#    num = 5/0
#except:
#    print("An error occured")
#    raise #Even though the exception is caught here, using raise by itself will actually print out the exception message that was generated when the error was caught

print("We also have a sanity check function, 'assertion'")
print(1)
print(2)
assert 1+2 == 3
assert (2+2 == 3),"4 does not equal to 3"
print("its a good idea to put assertion before a function to check for correct input, and after assertions to check for the correct type of output")

