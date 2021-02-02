# by GEEE3, February 2, 2021
# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too" "short")
print("life"+"is"+"too"+"short")

# 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too", "short")

# 한 줄에 결괏값 출력하기
# 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.
for i in range(10):
    print(i, end = ' ')