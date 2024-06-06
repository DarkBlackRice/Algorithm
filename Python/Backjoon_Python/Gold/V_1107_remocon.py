# 리모컨

def dfs(k, string):
    global ans

    if k >= 7:
        return

    now = int(string)
    now_cnt = abs(now - N) + k
    if now >= N and ans < now_cnt:
        return
    
    if now_cnt < ans:
        # print(string, now_cnt)
        ans = now_cnt
    
    for i in data:
        dfs(k+1, string+str(i))


N = int(input())
M = int(input())
if M:
    arr = list(map(int, input().split()))
else:
    arr = []
    
data = []
for i in range(10):
    if i not in arr:
        data.append(i)

ans = abs(N-100)
for i in data:
    dfs(1, str(i))

print(ans)