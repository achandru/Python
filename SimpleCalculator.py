#import random
class SimpleCalculator(object):
	"""docstring for ClassName"""
	def __init__(self, var1, var2):
		#super(ClassName, self).__init__()
		self.operand1 = var1
		self.operand2 = var2
		
	def add(self):
		self.result = self.operand1 + self.operand2
		return self.result

	def sub(self):
		self.result = self.operand2 - self.operand1
		return self.result

calc = SimpleCalculator(5,50)

print SimpleCalculator.add(calc)

print SimpleCalculator.sub(calc)
