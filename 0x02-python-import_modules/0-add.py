#!/usr/bin/python3
if _name_ == "_main_":
    import add_0

    sum = add_0.add
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, sum(a, b))")
