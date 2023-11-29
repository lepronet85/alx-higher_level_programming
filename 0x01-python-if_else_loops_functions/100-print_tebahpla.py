#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i)), end="")
    i -= 1
    print("{}".format(chr(i).upper()), end="")
