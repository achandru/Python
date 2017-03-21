#import random
class SimpleCalculator(object):
	"""docstring for ClassName"""
	def __init__(self, var1, var2):
		#super(ClassName, self).__init__()
		self.operand1 = var1
		self.operand2 = var2
		
	def add(self):
		self.result = self.var1+self.var2

	def sub(self):
		self.result = self.var2-self.var1

	calc = SimpleCalculator(5,5)

	print 'hi'

	print SimpleCalculator.add(calc)

	print 'hi2'

	print SimpleCalculator.sub(calc)
