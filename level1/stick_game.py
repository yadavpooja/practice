import random
n = 21
while True:
    a = int(input("Enter the number picked by user: "))
    n -= a
    if n == 1:
        print("comp lost")
        break
    b = random.randint(1,4)
    n -= b
    if n == 1:
        print("user lost")
        break

