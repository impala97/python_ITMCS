import sys
def main(arg=None):
    if arg is None:
        arg = sys.argv[1:]

    print("Number of arguments passed: %d " % len(arg))
    for i in arg:
        print(i)

if __name__ == "__main__":
    main()