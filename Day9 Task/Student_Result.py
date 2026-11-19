""" A school system calculates student results differently depending on available data. 
Create a Result class where a method can calculate the result using either two 
subjects or three subjects. 
"""

class Result:
    def total(self,a,b,c=0):
        print("Total = ",a+b+c)

r1 = Result()
r1.total(80,95)
r1.total(80,95,70)
