class Employee:
'Common base class for all employees'
empCount = 0
def __init__(self, name, salary):
	self.name = name
	self.salary = salary
	Employee.Count += 1
	def displayCount(self):
		print "Total Employee %d" %Employee.empCount
		def displayEmployee(self):
			print "Name: ",self.name,",salary: ",self.salary
			"This would create first object of Employee class"
			emp1 = Employee("Chandra",10000)
			"This would create second object of Employee class"
			emp2 = Employee("Sekar",20000)
			emp1.displayEmployee()
			emp2.displayEmployee()
			print "Total Employee %d" %Employee.empCount
