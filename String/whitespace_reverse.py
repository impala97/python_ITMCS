import sys
def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    org = input("enter long stirng : ")
    #org = "my name is mehta smit"
    reverse(org)

def reverse(org) :
    size = 1
    for i in org:
        if i == " ":
            size += 1

    top = 0
    arr = [""] * size

    for i in range(0,len(org)):
        if org[i] == " " and top < 4:
            top += 1
        else:
            arr[top] += org[i:i+1]

    print("org : %s" % org,end="\n")
    print("reverse : ",end="")
    for i in range(size-1,-1,-1):
        print(arr[i] ,end=" ")

if __name__ == "__main__":
    main()