#!/usr/bin/python3

alpha = 97

while (alpha <= 122):
    if (chr(alpha) != 'e' || chr(alpha) != 'q'):
        print("{}".format(chr(alpha)), end='')
    alpha = alpha + 1
