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
		