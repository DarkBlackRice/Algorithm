# 배열 돌리기

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, o_d = list(map(int,input().split()))
    o_arr = [list(map(int,input().split())) for _ in range(N)]

    # 방향을 통일하자
    if o_d < 0:
        o_d = 360 + o_d

    # 회전수를 구하자
    n_d = o_d//45
    

    # 이제 돌리자
    for d in range(n_d):
        n_arr = [[0]*N for _ in range(N)] # 돌린 결과물 받을 보드 초기화

        for i in range(N):
            if i == (N-1)//2: # 가운데 행만 예외처리
                for j in range(N):
                    n_arr[i][j] = o_arr[N-1-j][j]
            else:
                for j in range(N):
                    if j == i:
                        n_arr[i][j] = o_arr[(N-1)//2][j]
                    elif j == (N-1)//2:
                        n_arr[i][j] = o_arr[i][i]
                    elif j == N-1-i:
                        n_arr[i][j] = o_arr[i][(N-1)//2]
                    else:
                        n_arr[i][j] = o_arr[i][j]

        o_arr = n_arr # 한 번 돌릴 때 마다 꾸준히 업데이트

    for i in range(N):
        print(*o_arr[i])
    
