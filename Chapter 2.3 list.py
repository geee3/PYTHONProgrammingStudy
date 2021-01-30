# by GEEE3, January 30, 2021
# 리스트를 사용하면 1, 3, 5, 7, 9 숫자 모음을 다음과 같이 간단하게 표현할 수 있다.
odd = [1, 3, 5, 7, 9]
print("list odd =", odd)

# 리스트 역시 문자열처럼 인덱싱을 적용할 수 있다.
a = [1, 2, 3, ['a', 'b', 'c']]
print("When list a =", a)
print("a[0] =", a[0], "a[-1] =", a[-1], "a[-1][0] =", a[-1][0])

# 문자열과 마찬가지로 리스트에서도 슬라이싱 기법을 적용할 수 있다.
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
b = a[3:5]
print("When list a =", a)
print("a[3:5] =", b)

# 리스트 연산하기
# 1. 리스트 더하기.
a = [1, 2, 3]
b = ['a', 'b', 'c']
print("a =", a, "b =", b, "a + b =", a + b)

# 2. 리스트 반복하기.
a = [1, 2, 3]
print("a =", a, "a * 3 =", a * 3)

# 3. 리스트 길이 구하기.
a = [1, 2, 3]
print("lenth of list a =", len(a))

# 4. 리스트에서 값 수정하기.
a = [1, 2, 3]
b = [1, 2, 3]
b[1] = 0
print(a, "into", b)

# 5. del 함수 사용해 리스트 요소 삭제하기.
a = [1, 2, 3]
b = [1, 2, 3]
del b[1]
print(a, "into", b)

# 리스트 관련 함수들
# 1. 리스트에 요소 추가(append).
a = [1, 2, 3]
b = [1, 2, 3]
b.append(0)
print("append =", a, "into", b)

# 2. 리스트 정렬(sort).
a = [5, 1, 3, 2, 4]
b = [5, 1, 3, 2, 4]
b.sort()
print("sort =", a, "into", b)

# 3. 리스트 뒤집기(reverse).
a = [5, 1, 3, 2, 4]
b = [5, 1, 3, 2, 4]
b.reverse()
print("reverse =", a, "into", b)

# 4. 위치 반환(index).
a = [1, 2, 3]
print("When string a =", a, "index of 3 =", a.index(3))

# 5. 리스트에 요소 삽입(insert).
a = [1, 2, 3]
b = [1, 2, 3]
b.insert(1, 0)
print("insert(1, 0) =", a, "into", b)

# 6. 리스트에 요소 제거(remove).
# remove(a)는 리스트에서 첫 번째로 나오는 a를 삭제하는 함수이다.
a = [1, 2, 3, 1, 2, 3]
b = [1, 2, 3, 1, 2, 3]
b.remove(3)
print("remove =", a, "into", b)

# 7. 리스트에 요소 끄집어내기(pop).
# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
a = [1, 2, 3]
b = [1, 2, 3]
b.pop()
print("pop =", a, "into", b)

# 8. 리스트에 포함된 요소 x의 개수 세기(count).
a = [1, 2, 3, 1, 2, 3, 2]
print("When string a =", a, "number of 2 =", a.count(2))