# by GEEE3, February 1, 2021
# 만약 5000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가자
money = 3000
if money >= 5000:
    print("택시를 타자")
else:
    print("걸어가자")

'''
조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not아 있다,
각각의 연산자는 다음과 같이 동작한다
x or y : x와 y 둘중에 하나만 True이면 True
x and y : x와 y 모두 True이면 True
not x : x가 False이면 True
'''

# 만약 5000원 이상의 돈을 가지고 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가자
money = 3000
card = True
if money >= 5000 or card:
    print("택시를 타자")
else:
    print("걸어가자")

'''
x in (list, tuple, string) : ~안에 x가 있다면 True
x not in (list, tuple, string) : ~안에 x가 있다면 False
'''

pocket = ['aidpod', 'iphone', 'money']
if 'money' in pocket:
    print("택시를 타자")
else:
    print("걸어가자")

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타자
# 돈과 카드 모두 없다면 걸어가자
pocket = ['airpod', 'iphone']
card = True
if 'money' in pocket:
    print("택시를 타자")
elif card:
    print("택시를 타자")
else:
    print("걸어가자")
# 즉 elif는 이전 조건문이 거짓일 때 수행된다