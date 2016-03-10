#!/usr/bin/env python3
n = int(input("enter the number of students:"))
data = {} #store data
languages = ('physics', 'maths', 'history')
for i in range(0, n): #for n number of students
    name = raw_input('enter name of student %d:' % (i+1))
    marks = []
    for x in languages:
        marks.append(int(input('enter marks of %s: ' % x)))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("%s 's total marks %d" % (x,total))
if total < 120:
    print("%s failed" % x)
else:
    print("%s passed:" % x) 
