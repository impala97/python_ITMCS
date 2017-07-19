import sys
def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    n = int(input("get primes upto n number : "))
    prime(n)


def prime(n):
    noprimes = [j for i in range(2, 8) for j in range(i*2, n, i)]
    noprimes.sort()

    top = 0
    while top < len(noprimes)-1:
        if noprimes[top] == noprimes[top+1] :
            noprimes.remove(noprimes[top])
        else :
            top +=1

    primes = [x for x in range(2, n) if x not in noprimes]

    print(primes)
if __name__== "__main__":
    main()