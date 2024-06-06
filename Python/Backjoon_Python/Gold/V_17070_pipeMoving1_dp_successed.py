

N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
dp = [[(0,0,0)] for _ in range(N)]

dp[0].append((1,0,0))

for c in range(2, N):
    if room[0][c]:
        dp[0].append((0,0,0))
    else:
        row = dp[0][c-1][0]
        dp[0].append((row,0,0))


for r in range(1,N):
    for c in range(1, N):
        if room[r][c]:
            dp[r].append((0,0,0))
        else:            
            row = dp[r][c-1][0] + dp[r][c-1][2]
            col = dp[r-1][c][1] + dp[r-1][c][2]

            if room[r-1][c] or room[r][c-1]:
                diag = 0
            else:
                diag = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
            dp[r].append((row, col, diag))

# for d in dp:
#     print(*d)

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])