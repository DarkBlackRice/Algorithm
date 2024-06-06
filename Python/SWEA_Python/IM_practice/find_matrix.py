# 행렬 찾기

import sys; sys.stdin = open('find_matrix_input.txt')

def count_size(r, c):
    global count
    count += 1
    n, m = 0, 0 # 부분행렬 시작지점
    while (r < N) and mat[r][c]:
        r += 1
        n += 1
    r -= 1
    while (c < N) and mat[r][c]:
        c += 1
        m += 1
    r -= n-1
    c -= m

    for i in range(r, r+n):
        for j in range(c, c+m):
            mat[i][j] = 0

    size_list.append((n,m))


T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    r, c = 0, 0
    count = 0
    size_list = [] # 행, 열 순으로 append

    for r in range(N):
        for c in range(N):
            if mat[r][c]:
                count_size(r,c)

    visit = [0] * count
    print(f'#{t+1} {count}', end=' ')
    for _ in range(count):
        min_v = 10000
        index = 0
        for i in range(count):
            if not visit[i]:
                temp = size_list[i][0] * size_list[i][1]
                if min_v > temp:
                    min_v = temp
                    index = i
                elif min_v == temp and size_list[index][0] > size_list[i][0]:
                    index = i
        print(*size_list[index], end=' ')
        visit[index] = 1
    print()