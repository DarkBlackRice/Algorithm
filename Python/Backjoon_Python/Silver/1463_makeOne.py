# 1로 만들기

def dfs(tn, cnt):
    global ans
    if ans < cnt:
        return
    
    if tn == 1:
        ans = min(ans, cnt)
        return
    
    if tn % 3 == 0:
        dfs(tn//3, cnt + 1)

    if tn % 2 == 0:
        dfs(tn//2, cnt + 1)
    
    dfs(tn - 1, cnt + 1)


N = int(input())
ans = 1_000_000
dfs(N, 0)
print(ans)