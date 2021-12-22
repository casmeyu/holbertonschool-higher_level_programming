#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
#digit = abs(number) % 10
digit = int(math.fmod(number, 10))
answer = "Last digit of {:d} is {:d}".format(number, digit)
if (digit > 5):
    answer += " and is greater than 5"
elif (digit < 6 and digit != 0):
    answer += " and is less than 6 and not 0"
else:
    answer += " and is 0"

print("{}".format(answer))
