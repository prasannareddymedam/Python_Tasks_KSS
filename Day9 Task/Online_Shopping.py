""" An e-commerce company organizes products using multiple levels. Create classes 
Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
display product details.
"""

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self,name,price,warranty):
        Product.__init__(self,name,price)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def display(self):
        print(self.name,self.price,self.warranty)

m1 = MobilePhone("Samsung",20000,"1 Year")
m1.display()
