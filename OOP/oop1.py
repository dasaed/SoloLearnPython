#Object Oriented Programming
class Cat: #Class = object
	def __init__(self, color, legs) # most important method of a class, always include it
		self.color = color
		self.legs = legs

felix = Cat("ginger",4)
rover = Cat("dog-colored",4)
stumpy = Cat("brown",3)

print("This is the color of felix")
print(felix.color)
print("# of legs for stumpy")
print(stumpy.legs)


