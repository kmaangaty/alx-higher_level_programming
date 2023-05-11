#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_count = len(sys.argv) - 1
    if args_count == 0:
        print("{} arguments.".format(args_count))
    elif args_count == 1:
        print("{} argument.".format(args_count))
    elif args_count > 1:
        print("{} arguments.".format(args_count))
