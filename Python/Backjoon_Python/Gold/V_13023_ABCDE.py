# A B C D E

def dfs(v, k):
    global ans
    if k == 5:
        ans = 1
        return
    
    for w in graph[v]:
        if vst[w] == 0:
            vst[w] = 1
            dfs(w, k+1)
            vst[w] = 0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
vst = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(N):
    vst[i] = 1
    dfs(i, 1)
    if ans == 1:
        break
    vst[i] = 0
print(ans)