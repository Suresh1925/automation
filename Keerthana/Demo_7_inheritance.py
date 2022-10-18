# Calling function from other file
from Demo_6_OOPS import Calculator

class childImp(Calculator):
    num2=200

    def __init__(self): # Child constructor
        Calculator.__init__(self,2,5) # Making connection with other function # Parent constructor

    def getcompleteData(self):
        return self.num2 +self.addition()

obj = childImp()
print(obj.getcompleteData())