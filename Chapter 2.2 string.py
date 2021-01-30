# by GEEE3, January 30, 2021
# 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미한다.
# 문자열을 만들고 사용하는 방법.
# 1. 큰 따옴표(")로 양쪽 둘러싸기.
food = "Python's favorite food is perl"
print(food)

# 2. 작은 따옴표(')로 양쪽 둘러싸기.
say = '"Python is very easy." he says.'
print(say)

# 3. 큰 따옴표 또는 작은 따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기.
multiline = """Life is too short
You need python"""
print(multiline)

# 문자열 연산하기
# 1. 문자열 더해서 연결하기(Concatenation).
head = "Python"
tail = " is fun!"
body = head + tail
print(body, "= result of Concatenation")

# 2. 문자열 곱하기(Multistring).
print("=" * 50)
print("How to Multistring")
print("=" * 50)

# 3. 문자열 길이 구하기.
a = "Life is too short"
print(len(a), "= lenth of string 'Life is too short'")

# 문자열 인덱싱(Indexing)
# a[번호]는 문자열 a 안의 특정한 값을 뽑아낸다. 이를 인덱싱이라고 한다.
a = "Life is too short, You need Python"
print("String 'a' =", a)
print(a[0], "= first index of a")
print(a[12], "= 12nd index of a")
print(a[-1], "= last index of a")

# 문자열 슬라이싱(Slicing)
INFO = "20210130CLOUDY"
date = INFO[0:8]
weather = INFO[8:]
print("date =", date, "weather = ", weather)
# INFO[0:8]이 뜻하는 것은 문자열 INFO에서 0번째 ~ 7번째 문자를 뽑아낸다는 의미이다.
# INFO[8:]은 8번째 문자부터 마지막 문자까지를 뽑아낸다.

# 문자열 포매팅(Formatting)
# 1. 숫자 바로 대입.
a = "I eat %d apples." % 3
print(a)

# 2. 문자열 바로 대입.
a = "I eat %s apples." % "five"
print(a)

# 3. 숫자 값을 나타내는 변수로 대입.
number = 2
a = "I eat %d apples." % number
print(a)

# 4. 2개 이상의 값 넣기.
number = 10
day = "three"
a = "I ate %d apples. so I was happy for %s days." % (number, day)
print(a)

#format 함수를 사용한 포매팅
# 1. 숫자 바로 대입.
a = "I eat {0} apples." .format(3)
print(a)

# 2. 문자열 바로 대입.
a = "I eat {0} apples." .format("five")
print(a)

# 3. 숫자 값을 나타내는 변수로 대입.
number = 2
a = "I eat {0} apples." .format(number)
print(a)

# 4. 2개 이상의 값 넣기.
number = 10
day = "three"
a = "I ate {0} apples. so I was happy for {1} days." .format(number, day)
print(a)

# 5. 이름으로 넣기.
a = "I ate {number} apples. so I was happy for {day} days." .format(number = 10, day = "three")
print(a)

# 문자열 관련 함수들
# 1. 문자 개수 세기(count)
a = "MyPython"
print(a.count('y'), "= the number of character 'y' in 'Python'")

# 2. 위치 알려주기(find)
# 문자열 중 특정 문자가 맨 처음으로 나온 위치를 반환한다.
# 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
a = "Python is the best choice."
print("At string a,", a)
print(a.find('b'), "= location of character 'b'")
print(a.find('k'), "= there is no character 'k'")

# 3. 위치 알려주기(index)
# 문자열 중 특정 문자가 맨 처음으로 나온 위치를 반환한다.
# 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다.
a = "Life is too short."
print("At string a,", a)
print(a.index('t'), "= location of character 't'")

# 4. 소문자를 대문자로(upper), 대문자를 소문자로(lower) 바꾸기
a = "small python"
b = "BIG PYTHON"
print(a, "into", a.upper())
print(b, "into", b.lower())