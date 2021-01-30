# by GEEE3, January 30, 2021
# 숫자형(Number)이란 숫자 형태로 이루어진 자료형을 뜻한다.
# 정수형(Integer)은 정수를 뜻하는 자료형을 말한다.
a = -123
print(a, "= Integer datatype")

# 실수형(Floating-point)은 소수점이 포함된 숫자를 말한다.
a = 1.2
print(a, "= Floating-point datatype")

# 8진수(Octal)를 만들기 위해서는 숫자가0o 또는 0O로 시작하면 된다.
a = 0o177
print(a, "= Octal datatype")

# 16진수(Hexadecimal)를 만들기 위해서는 숫자가 0x로 시작하면 된다.
a = 0x8ff
print(a, "= Hexadecimal datatype")

# 숫자형을 활용하기 위한 연산자.
# 1. x의 y제곱을 나타내는 ** 연산자.
a = 3
b = 4
print(a ** b, "= result of 3 ** 4")

# 2. 나눗셈 후 나머지를 반환하는 % 연산자.
a = 7
b = 3
print(a % b, "= result of 7 % 3,", b % a, "= result of 3 % 7")

# 3. 나눗셈 후 몫을 반환하는 // 연산자.
a = 7
b = 4
print(a / b, "= result of 7 / 4,", a // b, "= result of 7 // 4")