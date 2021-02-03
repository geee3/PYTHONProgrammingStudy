# by GEEE3, February 3, 2021

'''
모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다
mod.py

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

if __name__ == '__main__':
    circle = Math()
    print(circle.solv(5))
'''

# import는 이미 만들어 놓은 파이썬 무듈을 사용할 수 있게 해주는 명령어이다
from mod import Math

circle = Math()
print("CIRCLE AREA =", circle.solv(10))