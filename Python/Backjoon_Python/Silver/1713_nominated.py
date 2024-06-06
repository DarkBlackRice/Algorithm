#다시 해봅시다

N = int(input())
recoTimes=int(input())
recoList=list(map(int,input().split()))

photoDict = {} # 추천 시작전에는 사진틀이 비어있다
#딕셔너리에 받을 자료의 포멧은 {후보번호:[득표 수, 순서]}
for number in range(recoTimes):    
    if recoList[number] in photoDict:
        photoDict[recoList[number]][0] += 1
        # 이미 게시되어있는데 추천받으면 추천횟수만 증가시킨다
    else: #이미 게시된 경우가 아니라면 '항상' 추가해야한다 (해당 득표 수 관련 x)
        if len(photoDict) == N: # 만약 사진틀 N개가 다 찼다면 -> 삭제시퀀스 시작
            minVoted =min(photoDict.values())[0] #가장 작은 투표수 서칭
            minVotedList = [key for key, value in photoDict.items() if value[0] == minVoted] # 추천수가 가장 적은 후보번호 리스트 받기
            oldest = recoTimes+100 #순서가 추천횟수+100 보다는 클 수 없음
            delList = 0
            for person in minVotedList: #모든 삭제후보들 대상으로
                if oldest > photoDict[person][1]: #순서 탐색 (숫자가 작을수록 오래된 것)
                    oldest = photoDict[person][1] #기존 가장 오래된 순서보다 작다면 갱신
                    delList = person #최종적으로 추천수가 가장 적고(o) 가장 오래된 학생(o)을 선정하여
            del photoDict[delList] #지우고
        
        photoDict[recoList[number]] = [1,number] #새 학생 게시

# 사진틀에서 빠진 학생은 추천수가 0으로 초기화된다 : 딕셔너리에서 제거되면서 추천수와 순서가 사라지니까 당연하다

finalList = photoDict.keys()
for person in sorted(finalList):
    print(person,end=" ")