""" A library stores information about books and digital books. Create a base class Book 
with a constructor to initialize book details. Create a derived class EBook that adds file 
size information. 
"""

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,title,author,file_size):
        Book.__init__(self,title,author)
        self.file_size = file_size

    def display(self):
        print(self.title,self.author,self.file_size)

b1 = EBook("Python", "Guido", "5MB")
b1.display()
