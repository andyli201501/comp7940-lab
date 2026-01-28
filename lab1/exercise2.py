# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
	for i in range (2, x):
		if x % i == 0:
			print (i)
#test number because it donot have a test number to test function
print_factor(52633)
