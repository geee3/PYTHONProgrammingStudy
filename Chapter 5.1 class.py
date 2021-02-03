# by GEEE3, February 2, 2021
# 사칙연산을 가능하게 하는 FourCal class
class FourCal:
    def __init__ (self, first, second):
        self.first = first
        self.second = second
    def setdata (self, first, second):
        self.first = first
        self.second = second
    def add(self):
        self.result = self.first + self.second
        return self.result
    def mul(self):
        self.result = self.first * self.second
        return self.result
    def sub(self):
        self.result = self.first - self.second
        return self.result
    def div(self):
        self.result = self.first / self.second
        return self.result

a = FourCal(23, 6)
print("a + b =", a.add())
print("a - b =", a.mul())
print("a * b =", a.sub())
print("a / b =", a.div())

# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        self.result = self.first ** self.second
        return self.result

b = MoreFourCal(23, 6)
print("a ^ b =", b.pow())