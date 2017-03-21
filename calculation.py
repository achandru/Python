import math
import random
class calculation(object):
	"""docstring for calculation"""
	def __init__(self, val1,val2):
		#super(calculation, self).__init__()
		self.operator1 = val1
		self.operator2 = val2

	def add(self):
		self.result = self.operator1 + self.operator2
		return self.result

	def sub(self):
		self.result = self.operator1 - self.operator2
		return self.result

	def mul(self):
		self.result = self.operator1 * self.operator2
		return self.result	
		
	def div(self):
		self.result = self.operator1 / self.operator2
		return self.result

	calc = calculation(50,5)

print calculation.add(calc)
print calculation.sub(calc)
print calculation.mul(calc)
print calculation.div(calc)