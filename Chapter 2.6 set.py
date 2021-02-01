# by GEEE3, February 1, 2021
# 집합 자료형은 set 키워드를 사용해 만들 수 있다.
# set 자료형은 중복을 허용하지 않고, 순서가 없다.
s1 = set([1, 2, 3])
s2 = set("Hello")
print("s1 =", s1, "s2 =", s2)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print("s1 =", s1, "s2 =", s2)

# 1. 교집합
print("Intersection =", s1 & s2)

# 2. 합집합
print("Sum of sets =", s1 | s2)

# 3. 차집합
print("difference of sets =", s1 - s2)

# 집합 자료형 관련 함수들
# 1. 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s2 = set([1, 2, 3])
s2.add(4)
print(s1, "into", s2)

# 2. 값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s2 = set([1, 2, 3])
s2.update([4, 5, 6])
print(s1, "into", s2)

# 3. 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s2 = set([1, 2, 3])
s2.remove(3)
print(s1, "into", s2)