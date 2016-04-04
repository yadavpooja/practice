basic_salary = 1500
n = int(input("Enter the number of camera sold: "))
t = int(input("Enter the total price of camera: "))
bonus = 200 *n
commision = t * 0.2
gross_salary = basic_salary + bonus +commision
print "Bonus is %d" % bonus
print "Commision is %d" % commision
print "Gross salary is %d" % gross_salary
