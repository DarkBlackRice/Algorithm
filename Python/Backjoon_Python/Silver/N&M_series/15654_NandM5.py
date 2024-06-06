# N 과 M (5)

def dfs(cnt, ser):
    if cnt == M:
        ans.append(ser)
        return

    for i in range(N):
        if  not visited[i]:
            visited[i] = True
            dfs(cnt+1, ser + [lst[i]])
            visited[i] = False

N, M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
visited = [False] * N
ans = []
dfs(0, [])
for a in ans:
    print(*a)
