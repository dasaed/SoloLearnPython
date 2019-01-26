#Object Oriented Programming

#############################################################
#############################################################
#############################################################
######## Examples from solo Learn #######
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


class A:
  def firstMethod(self):
    print("A method")
    
class B(A):
  def secondMethod(self):
    print("B method")
    
class C(B):
  def thirdMethod(self):
    print("C method")
    
ctest = C()
ctest.firstMethod()
ctest.secondMethod()
ctest.thirdMethod()
## Magic Methods ##
#
#Magic methods are special methods which have double underscores at the beginning and end of their names.
#They are also known as dunders.
#So far, the only one we have encountered is __init__, but there are several others.
#They are used to create functionality that can't be represented as a normal method.
#
#One common use of them is operator overloading.
#This means defining operators for custom classes that allow operators such as + and * to be used on them.
#An example magic method is __add__ for +.
#class Vector2D:
#  def __init__(self, x, y):
#    self.x = x
#    self.y = y
#  def __add__(self, other):
#    return Vector2D(self.x + other.x, self.y + other.y)
#
#first = Vector2D(5, 7)
#second = Vector2D(3, 9)
#result = first + second
#print(result.x)
#print(result.y)
#
#Magic Methods
#
#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |
#
#The expression x + y is translated into x.__add__(y).
#However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
#There are equivalent r methods for all magic methods just mentioned.Magic Methods
#
#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |
#
#The expression x + y is translated into x.__add__(y).
#However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
#There are equivalent r methods for all magic methods just mentioned.
#############################################################
#############################################################
#############################################################


class MyAnimal: #Class = object
    def __init__(self, color, legs): # most important method of a class, always include it
        self.color = color
        self.legs = legs

    def setColor(color):
        self.color = color
    def speak():
        print("I am an animal, I don't speak")
        self.lang = None



class Feline(MyAnimal):
    specie = "feline"
    def __init__(self,name,theType):
        self.name = name 
        self.theType = theType 
        self.legs =4

    def color(self,color):
        super.setColor(color)

    def speak(self):
        print("All cats purr!")
        self.lang = "purr"
    def speak(self,lang):
       self.lang = lang
       print(lang)

simba = Feline("Simba","Lion")
simba.color("yellow")
print(simba.color)
simba.speak()
simba.speak("roar")

class Vehicle:
    def information(self):
        """
        Speed =  how fast the vehicle goes
        wheels = number of wheels
        fuel = How much fuel per hour it consumes
        """
    def __init__(self):
        speed = 100
        wheels = 4
        fuel = 40
        wings = False
    def __init__(self,speed, wheels, wings, fuel):
        self.speed = speed
        self.wheels = wheels
        self.wings = wings
    def maxdistance():
        maxdistance = (speed/fuel)


class Plane(Vehicle):
    def fly(self):
        print("The plane is flying")


jet = Plane()
jet.wings = True
print (jet.fly())
