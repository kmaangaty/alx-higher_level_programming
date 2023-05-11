#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    args_count = len(sys.argv)
    for pos in range(args_count - 1):
        current_arg = sys.argv[pos + 1]
        sum = sum + int(current_arg)
    print("{}".format(sum))
