# by GEEE3, February 4, 2021

'''
try, except문의 기본 구조는 다음과 같다

try:
    ...
except[발생 오류[as 오류 메시지 변수]]:
    ...

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다
하지만 try 블록에서 오류가 발생하지 않았다면 except 블록은 수행되지 않는다
'''

try:
    a = [1,2]
    4 / 0
    print(a[3])
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

# 오류 회피하기
try:
    f = open("NONE.txt", 'r')
except FileNotFoundError:
    pass

# 예외 만들기
class myError(Exception):
    pass

def say_nick(nick):
    if nick == '귀염둥이':
        raise myError()
    print(nick)

say_nick("겸둥이")
say_nick("귀엽둥이")