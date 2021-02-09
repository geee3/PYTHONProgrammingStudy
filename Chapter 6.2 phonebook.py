# by GEEE3, February 9, 2021

'''
문제 설명
전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다
전화번호가 다음과 같을 경우 구조대 전화번호는 영석이의 전화번호의 접두사입니다

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phoneBook이 solution 함수의 매개변수로 주어질 때
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true를 return 하도록
solution 함수를 작성해주세요

제한사항
phoneBook의 길이는 1 이상 1,000,000 이하입니다
각 전화번호의 길이는 1 이상 20 이하입니다

입출력 예 설명
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.
1번째 전화번호 "12"가 2번째 전화번호 "123"의 접두사입니다. 따라서 답은 false 입니다.
'''

# Main solution function with 2 while loop
def solution(copyBook):
    copyBook.sort(key=len)
    count = 0

    while count < len(copyBook):
        another = count + 1
    
        while another < len(copyBook):
            if weAreSame(copyBook[count], copyBook[another]):
                return copyBook[count], copyBook[another]
            another += 1
        count += 1
    
    return False

# Return True if two strings are same, Return False if they are different
def weAreSame(shortStr, longStr):
    count = 0
    sameNum = 0

    while count < len(shortStr):
        if shortStr[count] == longStr[count]:
            sameNum += 1
        count += 1

    if len(shortStr) == sameNum:
        return True
    else:
        return False

# Print Result
def printResult(result, phoneBook):
    if result:
        number1 = int(result[0])
        number2 = int(result[1])
        index1 = int(phoneBook.index(result[0]) + 1)
        index2 = int(phoneBook.index(result[1]) + 1)
        print('%d번째 전화번호 "%d"가 %d번째 전화번호 "%d"의 접두사입니다. 따라서 답은 false 입니다.' % (index1, number1, index2, number2))
    else:
        print("한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.")

# case1
phoneBook = ["119", "97674223", "1195524421"]
copyBook = phoneBook.copy()
result = (solution(copyBook))
printResult(result, phoneBook)

# case2
phoneBook = ["123", "456", "789"]
copyBook = phoneBook.copy()
result = (solution(copyBook))
printResult(result, phoneBook)

# case3
phoneBook = ["12", "123", "1235", "567", "88"]
copyBook = phoneBook.copy()
result = (solution(copyBook))
printResult(result, phoneBook)