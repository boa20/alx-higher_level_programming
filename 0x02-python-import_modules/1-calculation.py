#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1

    add = calculator_1.add
    diff = calculator_1.sub
    prod = calculator_1.mul
    quo = calculator_1.div
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, diff(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, prod(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, quo(a, b)))
