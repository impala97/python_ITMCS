import sys
import math

def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]
    l = [i for i in range(0, 5)]
    l = reverse(l)

    print(l)

def reverse(l):

    ftop = 0
    ltop = len(l)-1

    fl = math.floor(len(l)/2)
    ll = math.ceil(len(l)/2)

    while ftop < fl and ltop > fl:
        l[ftop],l[ltop] = l[ltop],l[ftop]
        ftop += 1
        ltop -= 1

    return l
if __name__ == "__main__":
    main()