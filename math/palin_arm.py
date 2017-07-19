import sys

def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    number = int(input("enter number:"))

    print("1.palindrome")
    print("2.armstrong")
    choice = int(input("enter choice :"))

    if choice == 1 :
        palindrome(number)
    elif choice == 2:
        armstrong(number)
    else :
        print("invalid choice")

def palindrome(number) :
    n = number
    arm = 0

    while n != 0:
        tmp = int(n % 10)
        n = int(n / 10 )
        arm = arm * 10 +  tmp

    if arm == number :
        print("%d is palindrome number." % number)
    else :
        print("%d is not palindrome number." % number)

def armstrong(number):
    n = number
    palin = 0

    while n != 0 :
        tmp = int(n % 10)
        n = int(n / 10)
        palin += tmp * tmp * tmp

    if palin == number:
        print("%d is armstrong number.." % number)
    else :
        print("%d is not armstrong number" % number)

if __name__ == "__main__":
    main()