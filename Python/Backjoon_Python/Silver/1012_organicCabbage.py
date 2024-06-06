# 유기농 배추

from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]


def bfs(r, c):
    q = deque([(r,c)])
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 1:
                visited[nr][nc] = 0
                q.append((nr, nc))


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        visited[r][c] = 1
    
    cnt = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 1:
                cnt += 1
                bfs(r,c)

    print(cnt)
