 # github.com/www.programiz.com/coderbyte.com/Youtube

 print ('Hello Chand')
#-----------------------------------------------------------------
a = 3
b = 4
print  (a + b)
#-----------------------------------------------------------------
#IF else program
a=1 #variable declaration
if a==1:
	print"Correct"
else:
	print"Incorrect"
#-----------------------------------------------------------------
# Fibinocci program
# the sum of two elements defines the next
a, b = 0, 1
while b < 200:
       print b,
       a, b = b, a+b
#-----------------------------------------------------------------
b = 42
c = 23
a = b - c
print a
#-----------------------------------------------------------------
a=4
print a

b=12+5
print b

c=b%a
print c
#-------------------------------------------------------------------
cities = ['Bangalore','Chennai','Andhra','Kerala','Bengal','Delhi']
# Bad Way
i = 0
for city in cities:
	print(i,city)
	i += 1
#-------------------------------------------------------------------
cities = ['Bangalore','Chennai','Andhra','Kerala','Bengal','Delhi']
# Good Way
for i,city in enumerate(cities):
	print(i,city) 
#-------------------------------------------------------------------	
x_list = [1,2,3]
y_list = [2,4,6]
# Bad Way
for i in range(len(x_list)):
	y=x_list[i]
	x=y_list[i]
	print(x,y)
#-------------------------------------------------------------------	
x_list = [1,2,3]
y_list = [2,4,6]
# Good Way
for x,y in zip(x_list,y_list):
	print(x,y)
#-------------------------------------------------------------------
x = 10
y = -10
print('Before: x = %d,y = %d' %(x,y))
# Bad Way
tmp = y
y = x
x = tmp
print('After: x = %d,y = %d' %(x,y))
#--------------------------------------------------------------------
x,y = 10,-10
print('Before: x = %d,y = %d' %(x,y))
# Good Way
x,y = y,x
print('After: x = %d,y = %d' %(x,y))
#---------------------------------------------------------------------
ages = {
	'Chand' :23,
	'Mohan' :31
}
# Bad Way
if 'Kamal' in ages:
	age = ages['Kamal']
else:
	age = 'Unknown'
	print ('Kamal is %s years old' % age)
#----------------------------------------------------------------------	
ages = {
	'Chand' :23,
	'Mohan' :31,
	'Kamal' :43
}
# Bad Way
if 'Kamal' in ages:
	age = ages['Kamal']
else:
	age = 'Unknown'
	print ('Kamal is %s years old' % age)
#----------------------------------------------------------------------
ages = {
	'Chand' :23,
	'Mohan' :31,
	'Kamal' :43
}
# Good Way
age = ages.get('Kamal','Unknown')
print ('Kamal is %s years old' % age)
#------------------------------------------------------------------------
needle = 'd'
haystack = ['a','b','c','d']
# Bad Way
found = False # Marker Variable
for letter in haystack:
	if needle == letter:
		print('Found!')
		found= True
		break
	if not found:
		print('Not Found!')
#------------------------------------------------------------------------		
needle = 'd'
haystack = ['a','b','c','d']
# Good Way
for letter in haystack:
	if needle == letter:
		print('Found!')
		break
	else: # If no break Occurred
		print('Not Found!')
#-------------------------------------------------------------------------
# Bad Way
f = open('sam.py') # File Object 'f'
text = f.read()
for line in text.split('\n'):
	print(line)
	f.close()
#--------------------------------------------------------------------------			
# Another Way
f = open(sam.py)
for line in f:
	print(line)
	f.close()
#--------------------------------------------------------------------------
# Good Way
with open('sam.py') as f:
	for line in f:
		print(line)
#--------------------------------------------------------------------------			
# Bad Way
print('Converting!')
print(int('1'))
print('Done')
#---------------------------------------------------------------------------
# Better Way
print('Converting!')
try:
	print(int('1'))
except:
	print('Conversion Failed!')
else: # If- No-Except
	print('Conversion Successful!')
finally:
	print('Done!')
#----------------------------------------------------------------------------
STRING = "# This is String"

print STRING	
#----------------------------------------------------------------------------
i = 256*256
print i
#----------------------------------------------------------------------------
x = int(raw_input("Please Enter an Integer:"))
if x < 0:
	x = 0
	print 'Negative Value'
	elif x==0:
		print 'Zero'
	elif x==1:
		print 'Single'
	else x:
		print 'More'
#-----------------------------------------------------------------------------
# Measure the Length of String
a = ['Apple','Orange','PinApple']
for x in a:
print x,len(x) 		
#------------------------------------------------------------------------------
my = [1,2,3]
for i in my:
	print (i)
#------------------------------------------------------------------------------
def fib(n):
    a = 0
    b = 1
    for i in range(0, n):
	temp = a
	a = b
	b = temp + b
    return a

# Display the first 15 Fibonacci numbers.
for c in range(0, 25):
    print(fib(c))
#--------------------------------------------------------------------------------    	
input_num = input("\nEnter a Number:")
a,b,c = 0,0,1
if input_num == 1:
    print "The Number is 0"
else:
    fib = 1
    while fib < input_num:
      	a = b + c
       	b = c
      	c = a
      	fib = fib + 1
    print "The Number is : "+str(a)
#----------------------------------------------------------------------------------    
from collections import Counter
import string


def count_letters(word):
    global count
    wordsList = string.split(word)
    count = Counter()
    for words in wordsList:
        for letters in set(words):
            return count[letters]

word = "The grey old fox is an idiot word"
print count_letters(word)
#-------------------------------------------------------------------------------------#
user = raw_input("Enter the string: ")
print (user)[::-1]
#--------------------------------------------------------------------------------------
user = int(raw_input("Enter the value: "))

print("The decimal value of",user,"is:")
print(bin(user),"in Binary.")
print(oct(user),"in Octal.")
print(hex(user),"in Hexadecimal.")
#----------------------------------------------------------------------------------------