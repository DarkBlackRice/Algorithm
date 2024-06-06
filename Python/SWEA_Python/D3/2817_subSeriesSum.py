# 부분수열의 합

def dfs(n, sum_v):
    global cnt
    if sum_v > K:
        return
    if sum_v == K:
        cnt += 1
        return

    for i in range(n, N):
        dfs(i+1, sum_v + srs[i])


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    srs = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{t+1} {cnt}')
