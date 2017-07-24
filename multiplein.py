import sys

class intbase:
    def __init__(self,data=0):
        self.data = data
        print("data : %d" % data)


class strbase:
    def __init__(self,data=""):
        self.data = data
        print("data : %s" % data)


class derived(intbase,strbase):
    def __init__(self,data):
        super.__init__(self,data)



def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    print("derived class")
    d = strbase("smit")
    d1 = intbase(2561997)

if __name__ == "__main__":
    main()