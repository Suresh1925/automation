# def test(name):
#     print("fear"+name)
# test("facts")
#
# def add(a, b):
#     print(a + b)
# add(2, 4)
#
# def ret(a, b):
#     return a + b
# print(ret(3, 4))

# Classes and functions
class calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("the value is added")


    def add(self):
        return self.a + self.b + calculator.num


myobj = calculator(5, 9)
print(myobj.add())
myobj.num


