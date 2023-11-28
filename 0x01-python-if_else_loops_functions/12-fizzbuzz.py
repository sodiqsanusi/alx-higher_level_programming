#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        lilac = num
        if (num % 3 == 0) and (num % 5 == 0):
            lilac = "FizzBuzz"
        elif num % 5 == 0:
            lilac = "Buzz"
        elif num % 3 == 0:
            lilac = "Fizz"
        print(lilac, end=' ')
