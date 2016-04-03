#!/usr/bin/env python
number = int(input("Enter a number: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("number is multiple of 4")
    else:
        print("number is even")
else:
    print("Number is odd")
