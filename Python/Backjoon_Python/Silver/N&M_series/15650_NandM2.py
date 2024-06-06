# N 과 M (2)

def dfs(n, cnt, ser):
    if n == N:
        if cnt == M:
            ans.append(ser)
        return

    dfs(n+1, cnt+1, ser + [lst[n]])
    dfs(n+1, cnt, ser)
    

N, M = map(int, input().split())
lst = list(range(1,N+1))
ans = []
dfs(0,0,[])

for a in ans:
    print(*a)
