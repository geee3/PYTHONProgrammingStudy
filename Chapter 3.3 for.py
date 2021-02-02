# by GEEE3, February 2, 2021
# for문의 기본 구조는 다음과 같다
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# 리스트의 첫 번째 요소인 'one'이 먼저 변수 i에 대입된 후 print(i)를 수행한다
# 다음에 두 번째 요소 'two'가 변수 i에 대입된 후 print(i)를 수행하고 이것을 반복한다

# for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다
marks = [90, 25, 67, 80, 45]
for number in range(len(marks)):
    if marks[number] < 60:
        continue # 아래 문장을 수행하지 않고 for문으로 돌아감
    print("%d번 학생 축하합니다 A입니다." % (number + 1))

# 리스트 안에 for문을 포함하는 list comprehension을 사용하면 직관적인 프로그램을 만들수 있다
# 일반 문법은 다음과 같다 [표현식 for 항목 in 반복가능객체 if 조건문]
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)