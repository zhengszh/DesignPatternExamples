class Shape(object):
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def clone(self):
		raise NotImplementedError


class Rectangle(Shape):
	def __init__(self, x, y, color, width, height):
		super(Rectangle, self).__init__(x, y, color)
		self.width = width
		self.height = height

	def __str__(self):
		return "Rectangle %s %s %s %s %s" % (self.x, self.y, self.color, self.width, self.height)

	def clone(self):
		return Rectangle(self.x, self.y, self.color, self.width, self.height)

class Circle(Shape):
	def __init__(self, x, y, color, radius):
		super(Circle, self).__init__(x, y, color)
		self.radius = radius

	def __str__(self):
		return "Circle %s %s %s %s" % (self.x, self.y, self.color, self.radius)

	def clone(self):
		return Circle(self.x, self.y, self.color, self.radius)

shapes = []
circle = Circle(10, 10, "red", 20)
shapes.append(circle)
circle2 = circle.clone()
shapes.append(circle2)
rectangle = Rectangle(10, 10, "blue", 10, 20)
shapes.append(rectangle)
for s in shapes:
	print s
print "+++++++++++++++++++++++"
shape_copy = []
for s in shapes:
	shape_copy.append(s.clone())

for s in shape_copy:
	print s