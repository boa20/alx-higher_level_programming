#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

    add = add
    diff = sub
    prod = mul
    quo = div
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, diff(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, prod(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, quo(a, b)))
