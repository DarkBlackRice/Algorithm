# 부분집합의 합

def dfs(n, sum_elm, cnt):
    if n == NUMBER:
        if sum_elm == K and cnt == N:
            global ans
            ans += 1
        return 
    
    if sum_elm > K:
        return
    if cnt > N:
        return

    dfs(n+1, sum_elm + LST[n], cnt + 1)
    dfs(n+1, sum_elm, cnt)


NUMBER = 15
LST =   list(range(NUMBER,0,-1))
T = int(input())

for t in range(T):
    N, K = map(int,input().split())

    ans = 0
    dfs(0, 0, 0)
    print(f'#{t+1} {ans}')
    

