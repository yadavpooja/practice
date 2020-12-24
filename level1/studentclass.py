class Student():
    def __init__(self,name,branch,year):
        self.name = name
        self.branch = branch
        self.year = year

    def get_details(self):
        print self.name
        print self.branch
        print self.year



a = Student("ram", "ece",1)
b = Student("dove","cse",2)
a.get_details()
b.get_details()

