def GreetMe(): #Function Declaration
    print("Good Morning")

GreetMe() #Function calling

def GreetMe(name): #Function Declaration with argument
    print("Good Morning" + name)

GreetMe(" GCIT") #Function calling with value

def AddIntegers(a,b):
    print(a+b)
AddIntegers(2,3)

def AddIntegers(a,b):
    return a+b
print(AddIntegers(5,5))