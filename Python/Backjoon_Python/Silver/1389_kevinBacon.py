# 케빈 베이컨의 6단계 법칙

from collections import deque

def bfs(v):
    q = deque([v])
    vst[v] = 0
    while q:
        v = q.popleft()
        for w in graph[v]:
            if vst[w] == -1:
                vst[w] = vst[v] + 1
                q.append(w)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_v = 1000
min_idx = 0
for i in range(1,N+1):
    vst = [-1] * (N+1)
    bfs(i)
    tmp = 0
    for j in vst:
        if j == -1:
            continue
        tmp += j
    if min_v > tmp:
        min_v = tmp
        min_idx = i

print(min_idx)
