# 파리퇴치 3
import sys
input = sys.stdin.readline

def count_fly(row, col): # 파리 세는 함수 만들자

    c_count = x_count = board[row][col]

    for m in range(1,M):
        for d in range(4):
            n_xr = row + xr[d]*m # X자로 뿌렸을 때 
            n_xc = col + xc[d]*m
            if 0<=n_xr<N and 0<=n_xc<N:
                x_count += board[n_xr][n_xc]

            n_cr = row + cr[d]*m # +자로 뿌렸을 때
            n_cc = col + cc[d]*m
            if 0<=n_cr<N and 0<=n_cc<N:
                c_count += board[n_cr][n_cc]            
    
    return max(x_count,c_count) # 둘 충 큰 값 반환


T = int(input())

for t in range(T):
    N, M = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(N)]
    
    xr = [-1, 1, 1, -1] # X 탐색방향
    xc = [1, 1, -1, -1]

    cr = [-1, 0, 1, 0] # + 탐색방향
    cc = [0, 1, 0, -1]

    max_fly = -1
    for i in range(N):
        for j in range(N):
            temp = count_fly(i,j)
            if max_fly < temp:
                max_fly = temp

    print(f'#{t+1} {max_fly}')
