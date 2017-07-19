import sys
import math

def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    str = input("enter string : ")
    cipher = transposition(str)
    print("Plain text : ",str)
    print("cipher text :",cipher)

def transposition(str):
    if len(str) <= 1 :
        return str
    else :
        fhalf = str[0:math.ceil(len(str)/2)]
        shalf = str[len(fhalf):]

        return transposition(shalf) + transposition(fhalf)

if __name__ == "__main__":
    main()
