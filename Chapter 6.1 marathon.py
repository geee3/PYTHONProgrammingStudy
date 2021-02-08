# by GEEE3, February 8, 2021

'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다
단 한명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
마라톤을 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요

제한 사항
미리턴 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다
completion의 길이는 participant의 길이보다 1 작습니다
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다
참가자 중에는 동명이인이 있을 수 있습니다

입출력 예 설명
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
"vinko"는 참여자 명단에는 2명이 있지만, 완주자 명단에는 한명밖에 없기 때문에 한명은 완주하지 못했습니다.
'''

def solution(participant, completion):
    num = len(completion)
    copyParticipant = participant.copy()
    complete = 0

    while complete < num:
        participant.remove(completion[complete])
        complete += 1

    sameName = copyParticipant.count(participant[0])
    failure = participant[0]
    
    if sameName == 1:
        print('"%s"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.' % failure)
    else:
        print('"%s"는 참여자 명단에는 %d명이 있지만, 완주자 명단에는 한명밖에 없기 때문에 한명은 완주하지 못했습니다.' % (failure, sameName))

# case1
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
solution(participant, completion)

# case2
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)