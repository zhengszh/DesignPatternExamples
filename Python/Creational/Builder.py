class Item(object):
	def name(self):
		raise NotImplementedError

	def packing(self):
		raise NotImplementedError

	def price(self):
		raise NotImplementedError

class Packing(object):
	def pack(self):
		raise NotImplementedError

class Wrapper(Packing):
	def pack(self):
		return "Wrapper"

class Bottle(Packing):
	def pack(self):
		return "Bottle"

class Burger(Item):
	def packing(self):
		return Wrapper()

class Drink(Item):
	def packing(self):
		return Bottle()

class VegBurger(Burger):
	def price(self):
		return 25.0

	def name(self):
		return "Veg Burger"

class MeatBurger(Burger):
	def price(self):
		return 50.0

	def name(self):
		return "Meat Burger"

class Coke(Drink):
	def price(self):
		return 30.0

	def name(self):
		return "Coke"

class Pepsi(Drink):
	def price(self):
		return 35.0

	def name(self):
		return "Pepsi"

class Meal(object):
	def __init__(self):
		self.items = []

	def addItem(self, item):
		self.items.append(item)

	def getCost(self):
		return sum([item.price for item in self.items])

	def showItems(self):
		for item in self.items:
			print "Item: %s, Packing: %s, Price: %s" % (item.name(), item.packing().pack(), item.price())


class MealBuilder(object):
	def prepareVegMeal(self):
		meal = Meal()
		meal.addItem(VegBurger())
		meal.addItem(Coke())
		return meal

	def prepareNonVegMeal(self):
		meal = Meal()
		meal.addItem(MeatBurger())
		meal.addItem(Pepsi())
		return meal

builder = MealBuilder()
meal = builder.prepareVegMeal()
meal.showItems()
print "++++++++++++++++++++++++++++"
meal = builder.prepareNonVegMeal()
meal.showItems()