#!/usr/bin/env python3
class Customer():
    def __init__(self,name,accno,balance):
        self.name = name
        self.acc_no = accno
        self.balance = balance

    def withdraw(self,wa):
        self.wa = wa
        self.balance -= wa

    def add(self,amt):
        self.amt = amt
        self.balance += amt

    def checkstats(self):
        print("%s balance is %d.") % (self.name, self.balance)



ram = Customer("ram", 121, 100)
ram.checkstats()
ram.withdraw(50)
ram.checkstats()
ram.add(500)
ram.checkstats()
