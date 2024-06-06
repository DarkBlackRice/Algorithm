# 그래프 경로

def dfs(start,goal):
    v = start
    vst[v] = 1
    for w in gragh[v]:
        if w == goal:
            global flag
            flag = 1
            return
        if not vst[w]:
            dfs(w, goal)
    return


T = int(input())

for t in range(T):
    V, E = map(int,input().split())
    gragh = [[] for _ in range(V+1)]
    vst = [0] * (V + 1)
    for _ in range(E):
        s, e = map(int,input().split())
        gragh[s].append(e)
    S, G = map(int,input().split())
    flag = 0
    dfs(S, G)
    print(f'#{t+1} {flag}')