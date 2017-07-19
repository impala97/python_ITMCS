import sys

def main(args=None):
    if args is None:
        arg = sys.argv[1:]

    number = int(input("how long fibonacci series you want : "))

    fibo = [0,1]
    print(fibo[0],"\n",fibo[1])
    series = 0
    while number > series:
        series = fibo[0] + fibo[1]
        fibo[0] = fibo[1]
        fibo[1] = series
        if series <= number:
            print(series)

if __name__ == "__main__":
    main()