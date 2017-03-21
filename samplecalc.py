def add(a,b):
	return a + b
def sub(a,b):
	return a - b
def mul(a,b):
	return a * b
def div(a,b):
	return a / b

print ("Selected Option")
print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print ("4.Divition")

choice = raw_input("Enter Choice(1/2/3/4): ")
num1 = int(raw_input("Enter the first value: "))
num2 = int(raw_input("Enter the second value: "))
if choice == '1':
	print (num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
	print (num1,"-",num2,"=",sub(num1,num2))
elif choice == '3':
	print (num1,"*",num2,"=",mul(num1,num2))
elif choice == '4':
	print (num1,"/",num2,"=",div(num1,num2))
else:
	print ("Invalid Input")