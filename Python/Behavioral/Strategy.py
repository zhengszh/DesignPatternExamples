class Strategy(object):
	def doOperation(self, num1, num2):
		raise NotImplementedError

class OperationAdd(Strategy):
	def doOperation(self, num1, num2):
		return num1 + num2

class OperationSubtract(Strategy):
	def doOperation(self, num1, num2):
		return num1 - num2

class OperationMulitply(Strategy):
	def doOperation(self, num1, num2):
		return num1 * num2

class Context(object):
	def __init__(self, strategy):
		self.strategy = strategy

	def execute(self, num1, num2):
		return self.strategy.doOperation(num1, num2)

context = Context(OperationAdd())
print context.execute(10, 5)
context.strategy = OperationMulitply()
print context.execute(10, 5)
context.strategy = OperationSubtract()
print context.execute(10, 5)