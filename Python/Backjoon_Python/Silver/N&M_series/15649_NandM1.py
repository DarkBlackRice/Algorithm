# N과 M (1)

def dfs(cnt, ser):
    if cnt == M:
        ans.append(ser)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, ser + [lst[i]])
            visited[i] = False
    
N, M = map(int,input().split())
visited = [False] * N
lst = list(range(1,N+1))
ans = []
dfs(0, [])
for a in ans:
    print(*a)
