# 정사각형 방

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(row, col, cnt):
    global ans, ans_num
    visited[row][col] = case_visit
    flag = True
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < N) and (0 <= nc < N) and (visited[nr][nc] != case_visit) \
            and (room[nr][nc] == room[row][col] + 1):
            flag = False
            dfs(nr, nc, cnt + 1)
    if flag:
        if ans < cnt:
            ans = cnt
            ans_num = room[r][c]
        elif ans == cnt:
            ans_num = min(ans_num, room[r][c])


T = int(input())
for t in range(T):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0
    ans_num = 10000000
    case_visit = 0
    for r in range(N):
        for c in range(N):
            case_visit += 1
            dfs(r, c, 1)
    print(f'#{t+1} {ans_num} {ans}')
