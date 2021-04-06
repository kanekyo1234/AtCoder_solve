class Test():
    def init(self, a, b):
        self.num1 = a
        self.num2 = b


def func1(ins):
    ins.num1 += 50
    ins.num2 *= 10


test1 = Test(2, 6)
test2 = func1(test1)
num3 = test2.num1-test2.num2
print( num3)
