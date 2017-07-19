import sys

def oddEven(arg=None) :
	if arg is None :
		arg = sys.argv[1:]

	if number % 2 == 0 :
		print("Number %d is even number : " % number)
	else :
		print("Number %d is odd number : " %number)

if __name__ = "__main__" :
	oddEven()

	

