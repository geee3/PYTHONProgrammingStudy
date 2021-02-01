# by GEEE3, February 1, 2021
# 불 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
# 불 자료형은 True, False 2가지 값만을 가질 수 있다.
a = True
b = False
print("True =", type(a), "False =", type(b))

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 False가 되고 그렇지 않으면 True가 된다.
# 숫자에서는 그 값이 0일 때 False가 되며, None도 False를 의미한다.
print("bool([1, 2, 3]) =", bool([1, 2, 3]))
print("bool([]) =", bool([]))
print("bool(0) =", bool(0))
print("bool(15) =", bool(15))
print("bool(None) =", bool(None))