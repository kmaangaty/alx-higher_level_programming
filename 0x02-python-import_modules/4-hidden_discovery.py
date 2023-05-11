#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    vars = dir(hidden_4)
    for var in vars:
        if var[:2] != "__":
            print(var)
