#!/usr/bin/python3
upper = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - upper)), end='')
    if (upper == 0):
        upper = 32
    else:
        upper = 0
