# N 과 M (3)

def dfs(cnt, ser):
    if cnt == M:
        ans.append(ser)
        return

    for i in range(N):
        dfs(cnt+1, ser + [lst[i]])

N, M = map(int, input().split())
lst = list(range(1, N+1))
ans = []
dfs(0, [])
for a in ans:
    print(*a)