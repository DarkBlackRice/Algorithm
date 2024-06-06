# 파이프 옮기기 1 : dfs 실패

dr = [1, 0, 1]
dc = [0, 1, 1]

def dfs(r, c, d):
    global count

    # 이거 가지치기 가능할 것 같음
    # 안 될듯 ㅋㅋ

    if (r, c) == (N-1, N-1):
        count += 1
        return
     
    for i in range(3):
        if d<2 and d+i == 1:
            continue
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < N) and (0 <= nc < N) and (room[nr][nc] != 1) and \
            ((i != 2) or (room[nr-1][nc] != 1 and room[nr][nc-1] != 1)):
            nd = i
            visited[nr][nc] = 1
            dfs(nr, nc, nd)
            visited[nr][nc] = 0


N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = visited[0][1] = 1
count = 0
dfs(0,1,1) # 세로 : 0, 가로 : 1, 대각선 : 2, 감자 : 3
print(count)