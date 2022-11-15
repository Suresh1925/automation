class Calculator:   #its an blueprint to create an object
    num = 100

    def getData(self): #to access the method
        print("My name is praveen")


a = Calculator() #variable creation for class
a.getData()  #To call a function using a variable
print(a.num)
