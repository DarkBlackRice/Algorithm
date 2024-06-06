# 중간값 구하기

n = int(input())
midOfN = (n+1)//2

numList = map(int,input().split())
sortedNumList = sorted(numList)

print(sortedNumList[midOfN-1])

#걸린 시간 00:06:40