# 인구 이동

def ally(row, col):
    union = []
    stack = []
    visited[row][col] = True
    while True:

        dead_end = True    
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if (0<=nr<N and 0<=nc<N) and (not visited[nr][nc]) and\
                (L<=abs(LAND[row][col] - LAND[nr][nc])<=R):
                dead_end = False
                stack.append((row, col))
                if not union:
                    union.append(LAND[row][col])
                    union.append((row,col))
                union[0] += LAND[nr][nc]
                union.append((nr, nc))
                row, col = nr, nc
                visited[nr][nc] = True
                break

        if dead_end:
            if stack:
                row, col = stack.pop()
            else:
                break         

    return union


N, L, R = map(int,input().split())
LAND = [list(map(int,input().split())) for _ in range(N)]

flag = True
count = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# print('지도 : ')
# for country in LAND:
#     print(*country)
# print()

while flag:

    visited = [[False] * N for _ in range(N)]
    unions = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                temp = ally(r, c)
                if temp:
                    unions.append(temp)
    
    # print('연합 정보 : ')
    # for u in unions:
    #     print(*u)
    
    if unions:
        count += 1
        for u in unions:
            union_num = len(u)
            avg = u[0] // (union_num - 1)
            for i in range(1, union_num):
                tr, tc = u[i]
                LAND[tr][tc] = avg
    else:
        flag = False
    
    # print('지도 : ')
    # for country in LAND:
    #     print(*country)

print(count)

    
