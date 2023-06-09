#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        i = 1
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
