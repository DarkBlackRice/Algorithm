#백만장자 프로젝트

T = int(input())

for t in range(T):
    N = int(input())
    priceList = list(map(int,input().split()))
    n=0
    arbit = 0

    while n<N:
        maxIndex = n
        # maxIndex = priceList[n:].index(max(priceList[n:]))
        # 슬라이싱을 쓰면 안되는 이유 : 인덱스 초기화 -> 우리는 끝까지 인덱스를 유지하고 싶은데, 자르면 불편함
        #-> 따라서 이 방식을 쓸 때에는 리스트를 우선 전체적으로 참조할 필요 있음
        for i in range(n+1,N): 
            if priceList[i]>priceList[maxIndex]:
                maxIndex = i
        for i in range(n,maxIndex):
            arbit += priceList[maxIndex]-priceList[i]
        n = maxIndex+1
        
        #이건 구조 전체를 외우는게 좋을듯;
    print(f"#{t+1} {arbit}")