# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
	for i in range (2, x):
		if x % i == 0:
			print (i)

#test num because it donot have a test number to test function which cannot 
# know the function can run or not
print_factor(52633)

