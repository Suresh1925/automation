from class1 import calculator


class child1(calculator):
    no1 = 45
    def __init__(self):
        calculator.__init__(self, 3,9)
        print('child_1 class')

    def complete_data(self):
        return self.no + self.no1 + self.sum()


c1 = child1()
print(c1.complete_data())

