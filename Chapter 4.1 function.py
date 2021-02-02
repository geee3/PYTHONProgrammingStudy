# by GEEE3, February 2, 2021
# 여러 개의 parameter를 받는 함수 만들기.
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

add = add_mul('add', 1, 2, 3, 4, 5)
mul = add_mul('mul', 1, 2, 3, 4, 5)

print("When choice is add =", add)
print("When choice is mul =", mul)

# 키워드 파라미터 kwargs.
# print_kwargs 함수는 매개변수 kwargs를 출력하는 함수이다.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = 'Elise', age = 25)
# 매개변수 이름 앞에 **를 붙이면 매개변수는 딕셔너리가 되고 모든 key = value 값이 저장된다.

# 매개변수에 초깃값 미리 설정하기.
def tell_yourself(name, age, human = True):
    print("이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if human:
        print("사람입니다.")
    else:
        print("요정입니다.")

tell_yourself('Elise', 25, False)
tell_yourself('Sujin', 24)
# human 변수에 입력값을 주지 않았지만 초깃값 True를 갖게 된다.