import sys

global str 
str = "global scope"

def main(arg=None):
	if arg is None:
		arg = sys.argv[1:]

	str = "from local scope"
	print(str)

	global_scope()

def nonlocal_scope():
	nonlocal str 
	str = "nonlocal string"
	print(str)

	
if __name == "__main__":
	main()
