#최대수 구하기

n = int(input())

for i in range(n):
    numList=list(map(int,input().split()))
    sortedNumList=sorted(numList)
    print('#%d %d'%(i+1,sortedNumList[-1]))

#걸린 시간 00:02:14
#테스트 케이스 양식 그대로 들고와서 시간이 훨씬 덜들었다.