#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv

    print("{} argument{}{}".format(len(argv) - 1,
                                   "s" if len(argv) != 2 else "",
                                   ":" if len(argv) > 1 else "."))
    i = 1
    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i += 1
