# by GEEE3, February 2, 2021

'''
파일을 생성하기 위해 파이썬 내장 함수 open을 사용한다
open 함수는 "파일 이름"과 "파일 열기 모드"를 입력값으로 받고 파일 객체를 돌려준다

파일 열기 모드
r : 파일을 읽기만 할 때 사용
w : 파일에 내용을 쓸 때 사용
a : 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
'''

# 파일을 쓰기 모드로 열어 출력값 적기
f = open('NEW.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
f = open('NEW.txt', 'r')
line = f.read()
print(line)
f.close()

# 파일에 새로운 내용 추가하기
f = open('NEW.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

f = open('NEW.txt', 'r')
line = f.read()
print(line)
f.close()