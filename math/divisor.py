import sys

def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    number = int(input("enter number:"))
    divisor(number)

def divisor(number):
    div = [None] * 10
    top = 0

    print("Divisor of %d Number ; " % number)
    for i in range(1,number) :
        if number % i == 0 :
            div[top] = i
            top +=1

    for i in div:
        if i != None:
            print(i)

if __name__ == "__main__":
    main()
