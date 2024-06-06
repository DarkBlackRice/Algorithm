# N 과 M (4)

def dfs(n, cnt, ser):
    if cnt == M:
        ans.append(ser)
        return

    for i in range(n, N):
        dfs(i, cnt+1, ser+[lst[i]])
        
        
N, M = map(int, input().split())
lst = list(range(1,N+1))
visited = [False] * N
ans = []
dfs(0, 0, [])
for a in ans:
    print(*a)
