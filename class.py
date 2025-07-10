'''class Person:
    name="Ayush"
    Occupation="student"
    networth=0
    def info(self):
        print(f"{self.name} is a {self.Occupation} having networth: {self.networth}")
a=Person()
#a.name="kourav"
#a.Occupation="student"
#a.networth="10cr"
a.info()'''

#class methods
class Employee():
    company="tesla"
    def __init__(self,name):
        self.name=name
   #@classmethod
    def newcomp(self,company):
        self.company=company

    def showdetails(self):
        print(f"hello {self.name} and your company is {self.company}")
e1=Employee("Ayush")
e1.newcomp("Apple")
e1.showdetails()
print(Employee.company)