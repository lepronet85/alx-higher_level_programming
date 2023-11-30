#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv

    print("{} arguments{}".format(len(argv) - 1,
                                  ":" if len(argv) > 1 else "."))
    i = 1
    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i += 1
