class Library:
    def __init__(self):
        self.nbooks=0
        self.books=[]
    def addbooks(self,book):
        self.books.append(book)
        self.nbooks=len(self.books)
    def show(self):
        print(f"Library has {self.nbooks} book\nThe books are:") 
        for i in enumerate(self.books):
            print(i)
b1=Library()
b1.addbooks("harry potter")
b1.addbooks("Encyclopedia")
b1.addbooks("Junglebook")
b1.show()