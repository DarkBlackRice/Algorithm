#숫자 배열 회전

T = int(input())


for t in range(1,T+1):
    N = int(input())
    arr_90 = []
    arr_180 = []
    arr_270 = []
    for i in range(N):
        arr_90.append([0]*N)
    for i in range(N):
        arr_180.append([0]*N)
    for i in range(N):
        arr_270.append([0]*N)

    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range (N): #90도
        for j in range(N):
            arr_90[i][j]=arr[N-1-j][i]

    for i in range (N): #180도
        for j in range(N):
            arr_180[i][j]=arr[N-1-i][N-1-j]

    for i in range (N): #270도
        for j in range(N):
            arr_270[i][j]=arr[j][N-1-i]

    print('#%d'%t)
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j],end='')
        print('',end=' ')
        for j in range(N):
            print(arr_180[i][j],end='')
        print('',end=' ')
        for j in range(N):
            print(arr_270[i][j],end='')
        print()