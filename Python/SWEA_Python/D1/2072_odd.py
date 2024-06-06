# 홀수만 더하기

n = int(input())

for i in range(n):
    sumOfNums = 0
    numList=list(map(int,input().split()))
    for num in numList:
        if num%2==1:
            sumOfNums += num
    print('#%d %d'%(i+1,sumOfNums))
    
#걸린 시간 00:05:08