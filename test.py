import sys
import os

class employee:
	def_init_(self,first,last,pay)
	self.first = first
	self.last = last
	self.pay = pay
	self.email = first + '.' + last +'@company.com'

	def  fullname(self):
		return '{} {}'.format(self.first,self.last)

	emp_1 = employee('chand','sekar',50000)
	emp_2 = employee('kalai','selvi',20000)

	emp_1.fullname()
	print(employee.fullname(emp_1))