import sys

class A(object):
	def __init__(self,c=[0,0]):
		self.c = c

class B(A):
	def __init__(self):
		super(B,self).__init__()
class c :
	def main(arg=None):
		if(arg is None):
			arg = sys.argv[1:]

		a = A()
		b = B()

		print(a.c," ",b.c)
		a.c[1] = 3

		print(a.c," ",b.c)

	if __name__ == "__main__":
		main()
