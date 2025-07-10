class Student:
    def __init__(self, name):
        self.name = name

    def showname(self):
        print(f"Name of the student is: {self.name}")

class Id(Student):
    def __init__(self, name, id):
        super().__init__(name)  # Call the constructor of Student
        self.id = id

    def showid(self):
        print(f"Name of the student is: {self.name} and his ID: {self.id}")

# Creating instances
e1 = Student("Ayush")
e1.showname()

e2 = Id("Ayush", 10)
e2.showid()
