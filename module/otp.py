'''
upper case : 65-91
lower case : 97-123
symbol : @ # _ .
'''

import sys
import random
import cipher.trans_permut

getotp = cipher.trans_permut.transposition

def main(arg=None):
    if arg is None :
        arg = sys.argv[1:]

    #priority = int(input("How strong your password rate it out of 5 : "))
        generate_otp()

def generate_otp():

    symbol = ['@','#','_','.']
    otp = ""
    for i in range(1,3):
        otp +=chr(random.randint(65,90))
        otp +=chr(random.randint(97, 122))
        otp += str(random.randint(0,9))

    otp = getotp(otp)
    print("otp : ",otp)

if __name__ == "__main__":
    main()
