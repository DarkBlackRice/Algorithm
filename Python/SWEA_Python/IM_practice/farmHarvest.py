#농작물 수확하기

T = int(input())
for t in range(T):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    harvest = 0
    mid = N//2
    for r in range(mid+1):
        for c in range(mid-r,mid+r+1):
            harvest += farm[r][c]
    for r in range(1,mid+1):
        for c in range(r,N-r):
            harvest += farm[mid+r][c]
    print(f'#{t+1} {harvest}')