import self as self

from test_scripts.function_demo import calculator


class childclass(calculator):
    num2 = 200
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def get_parentvalue(self):
        return calculator.add() + childclass.num2


print(childclass.num2)
print(childclass.get_parentvalue(self))