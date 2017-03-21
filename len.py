#import getpass
print ("Welcome to SBI Bank")
password = 1234
depAmt = 60000
userPassword = input("Enter your Password :")
if (userPassword == password):
	amount = input("Enter the Amount :")
	if (amount > depAmt):
		print "You are Eligible Only 60000"
	elif (amount <= depAmt):
		print 'depAmt',depAmt
		print "Thanks for Visiting Collect Your Cash"
		Balance = int(depAmt)-int(amount)
		print 'Balance', Balance
elif (userPassword != password):
		print "Password Mismatch"
