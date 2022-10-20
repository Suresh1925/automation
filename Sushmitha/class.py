

class maths:

    no = 65

    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.f = f
        print('1st value is or value of a is  ',a)
        print('1st value is or value of b is  ',b)

    # def add(self, c):
    #
    #     c = a + b
    #     print(c)
    #
    # def sub(self):
    #     d = a - b
    #     print(d)
    #
    # def mul(self):
    #     e = a * b
    #     print(e)
    #
    # def div(self):
    #     self. f = self. a / self. b
    #     print(f)
    def ret(self):
        return self.a + self.b + maths.no



m = maths(6,2)
# m.div()
# m.add()
# m.sub()
# m.mul(2,7)
print(m.ret())

# m1=maths()
# m1.add(34,90)
# m1.mul(5,6)