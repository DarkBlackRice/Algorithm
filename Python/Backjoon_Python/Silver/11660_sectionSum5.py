# 구간합 구하기 5

import sys; input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    for j in range(1, N):
        dp[i][j] = arr[i][j] + dp[i][j-1] + dp[i-1][j] -dp[i-1][j-1]

for t in range(M):
    sr, sc, er, ec = map(lambda x : int(x) - 1, input().split())
    ans = dp[er][ec]
    if sr > 0 and sc > 0:
        ans = ans + dp[sr-1][sc-1] - dp[sr-1][ec] - dp[er][sc-1]
    elif sr > 0:
        ans -= dp[sr-1][ec]
    elif sc > 0:
        ans -= dp[er][sc-1]
    print(ans)