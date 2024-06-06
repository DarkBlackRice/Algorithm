
for i in range(10):
    n=int(input())
    vilList=list(map(int,input().split()))
    result = 0

    for j in range(2,n-2):
        nearList=[]
        for k in [-2,-1,1,2]:
            nearList.append(vilList[j+k])
        tall=max(nearList)
        if vilList[j]>tall:
            result+=(vilList[j]-tall)

    print('#%d %d'%(i+1,result))
