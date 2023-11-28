#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % -10 if number < 0 else number % 10
first = f"Last digit of {number} is {lastdigit}"
if lastdigit > 5:
    last = " and is greater than 5"
elif lastdigit == 0:
    last = " and is 0"
else:
    last = " and is less than 6 and not 0"
print(first + last)
