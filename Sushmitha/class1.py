class calculator:

    no = 65

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(('auto executing function'))

    def getinfo(self):
        print('general info')

    def sum(self):
        return self.a + self.b + calculator.no



c = calculator(8,6)
c.getinfo()
print(c.no)
print(c.sum())