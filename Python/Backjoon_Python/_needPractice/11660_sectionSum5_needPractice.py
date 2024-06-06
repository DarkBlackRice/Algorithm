# 구간합 구하기 5
import sys ; input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# sum_coord = [list(map(lambda x : int(x)-1 ,input().split())) for _ in range(M)]
dp = []

for m in range(M):
    s_r, s_c, e_r, e_c = map(int ,input().split())
    # if :
    sum_v = 0
    for r in range(s_r-1, e_r):
        for c in range(s_c-1, e_c):
            sum_v += board[r][c]
    print(sum_v)