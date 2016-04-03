n = int(input("Enter a number: "))
i = 1
a = []
for i in range(1,n/2+1):
    if n % i == 0:
        a.append(i)
print a

