#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("{}".format(0))
    else:
        i = 1
        n = 0
        for i in range(len(sys.argv) - 1):
            n = n + int(sys.argv[i + 1])
        print("{}".format(n))
