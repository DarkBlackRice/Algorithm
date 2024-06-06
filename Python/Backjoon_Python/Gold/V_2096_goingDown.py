# 내려가기

srch = ((0,1),(0,1,2),(1,2))

N = int(input())
arr = list(map(int, input().split()))
dp = [[],[]]
for a in arr:
    dp[0].append(a)
    dp[1].append(a)
for _ in range(N-1):
    ndp = [[],[]]
    arr = list(map(int, input().split()))
    for i in range(3):
        min_lst = []
        max_lst = []
        for j in srch[i]:
            max_lst.append(dp[0][j] + arr[i])
            min_lst.append(dp[1][j] + arr[i])
        ndp[0].append(max(max_lst))
        ndp[1].append(min(min_lst))
    dp = ndp
print(max(dp[0]), min(dp[1]))

