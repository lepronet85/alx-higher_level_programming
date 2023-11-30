#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    result = 0
    for i in range(len(args)):
        result += int(args[i])
    print(result)
