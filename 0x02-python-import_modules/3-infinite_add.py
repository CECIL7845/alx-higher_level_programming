#!/usr/bin/python3
def add_arg(argv):
    m = len(argv) - 1
    if m == 0:
        print("{:d}".format(n))
        return
    else:
        x = 1
        add = 0
        while x <= m:
            add += int(argv[x])
            x += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
