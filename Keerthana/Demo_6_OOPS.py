#Classes are user defined blueprint or prototype
#self keyword is mandatory for calling names into method
#instance and class variable have whole different purpose
#constructor name should be __init__

class Calculator:
    num = 100 # class variable
    def __init__(self,a,b): # defult constructor
        self.a=a
        self.b=b
        print("Called automatically when object is created") 

    def getData(self):
        print("Method in class")

    def addition(self):
        return self.a + self.b + Calculator.num

a=Calculator(2,3) # object creation # object 1
a.getData() # to call fun inside class
print(a.num) # call variable inside class

 
b=Calculator(4,5) # object creation # object 2
b.getData() # to call fun inside class
print(b.num)

