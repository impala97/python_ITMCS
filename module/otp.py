'''
upper case : 65-91
lower case : 97-123

'''

import sys
import random
import transposition

def main(arg=None):
    if arg is None :
        arg = sys.argv[1:]

    #priority = int(input("How strong your password rate it out of 5 : "))
    for i in range(0,20):
        generate_otp()

def generate_otp():

    #symbol = ['@','#','_','.']
    otp = ""
    for i in range(1,3):
        otp +=chr(random.randint(65,90))
        otp +=chr(random.randint(97, 122))
        otp += str(random.randint(0,9))

    #otp = transposition.transposition(otp)
    print("otp : ",otp)

if __name__ == "__main__":
    main()
