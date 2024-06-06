# 구간 합 구하기 5

import sys ; input = sys.stdin.readline

def sum_mtx(start_cor, end_cor):
    s_r, s_c = start_cor
    r, c = end_cor

    
    while True:
        sum_v = 0
        for c in range(s_c, c+1):
            sum_v += board[r][c]
        
        if r == s_r:            
            return sum_v
        
        else:
            return sum_v + sum_mtx(start_cor, (r-1, c))


N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# sum_coord = [list(map(lambda x : int(x)-1 ,input().split())) for _ in range(M)]

for m in range(M):
    s_r, s_c, e_r, e_c = map(lambda x : int(x)-1 ,input().split())
    s_tpl, e_tpl = (s_r, s_c), (e_r, e_c)
    print(sum_mtx(s_tpl, e_tpl))


