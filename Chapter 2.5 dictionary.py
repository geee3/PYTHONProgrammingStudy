# by GEEE3, January 31, 2021

'''
people이라는 단어에 사람, baseball이라는 단어에 야구라는 뜻이 부합되듯이,
딕셔너리(Dictionary)는 Key와 Value를 한 쌍으로 갖는 자료형이다
딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다
baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라,
baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다

다음은 기볻 딕셔너리의 모습이다
{Key1 : Value1, Key2 : Value2, Key3 : Value3, }
'''

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a['name'] = 'GEEE3'
a[3] = [1, 2, 3]
print("Dictionary a =", a)

# 딕셔너리 요소 삭제하기
del a['name']
print("Dictionary a =", a)

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'James' : 'A', 'Elise' : 'B'}
print("Grade of James =", grade['James'])

# 딕셔너리 관련 함수들
# Key 리스트 만들기(keys)
a = {'name' : 'Elise', 'phone' : '0123456789', 'birth' : '0102'}
print(a.keys())
# a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다
# 만약 반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다

# Value 리스트 만들기(values)
print(a.values())

# Key, Value 쌍 얻기(items)
print(a.items())

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print("print name in a =", 'name' in a)
print("print adress in a =", 'adress' in a)