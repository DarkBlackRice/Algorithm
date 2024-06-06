# 배열 돌리기 1

import sys
input = sys.stdin.readline

# 함수부

def rotate(row,col,arr):
    temp_arr = [[0]*col for _ in range(row)]

    for i in range(min(N,M)//2):
        for c in range(i,(M-1)-i):
            temp_arr[i][c] = arr[i][c+1]
            temp_arr[(N-1)-i][c+1] = arr[(N-1)-i][c]
        for r in range(i,(N-1)-i):
            temp_arr[r][(M-1)-i] = arr[r+1][(M-1)-i]
            temp_arr[r+1][i] = arr[r][i]

    return temp_arr


# 실행부

N, M, R = map(int,input().split())

input_arr = [list(map(int,input().split())) for _ in range(N)]

for r in range(R):
    input_arr = rotate(N,M,input_arr)

for i in range(N):
    print(*input_arr[i])