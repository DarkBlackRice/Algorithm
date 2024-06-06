#두 개의 숫자열

T = int(input())

for i in range(T):
    N,M = tuple(map(int,input().split()))
    NList=list(map(int,input().split()))
    MList=list(map(int,input().split()))
    print(NList)
    print(MList)
    if N>M:
        diff=N-M
        multiList=[]
        for j in range(diff+1):
            multi=0
            for k in range(M):
                multi += NList[j:][k]*MList[k]
            multiList.append(multi)
            print('멀티리스트 확인 : ',multiList)
        print('#%d %d'%(T,max(multiList)))
    elif M>N:
        diff=M-N
        multiList=[]
        for j in range(diff+1):
            multi=0
            for k in range(N):
                multi += NList[k]*MList[j:][k]
            multiList.append(multi)
            print('멀티리스트 확인 : ',multiList)
        print('#%d %d'%(T,max(multiList)))