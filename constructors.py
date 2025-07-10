'''class Person:
    def __init__(self,n,o,nw):#constructor
        self.name=n
        self.Occupation=o
        self.networth=nw
    
    def info(self):
        print(f"{self.name} is a {self.Occupation} having networth: {self.networth}")
a=Person("aysuh","student","10cr")
#a.name="kourav"
#a.Occupation="student"
#a.networth="10cr"
a.info()'''

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        
       
    return mfx


@greet      
def hrllo():
    print("Hello World!")

hrllo()
