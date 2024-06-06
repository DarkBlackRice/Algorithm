# 부분 수열의 합

def dfs(k, total, size):
    global cnt
    if k == N:
        if total == S and size > 0:
            cnt += 1
        return
    
    if total + memo[0][k] < S:  # 여태까지의 합에 아무리 양수만 골라 더해도 목표치보다 작을 때
        return
    if total + memo[1][k] > S:  # 여태까지의 합에 아무리 음수만 골라 더해도 목표치보다 클 때
        return
    
    dfs(k+1, total+arr[k], size+1)
    dfs(k+1, total, size)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
minus = 0 
plus = 0
memo = [[0] * N for _ in range(2)]
# 0행은 이후 양수부의 합
# 1행은 이후 음수부의 합

for i in range(N):
    if arr[i] < 0:
        minus += arr[i]
    else:
        plus += arr[i]

for i in range(N):
    memo[0][i] = plus
    memo[1][i] = minus
    if arr[i] < 0:
        minus -= arr[i]
    else:
        plus -= arr[i]
    
cnt = 0
dfs(0, 0, 0)
print(cnt)
