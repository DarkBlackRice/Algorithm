# 백준 1987 알파벳 dfs 시간초과

# import sys
# input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] not in alpha:
            alpha.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            alpha.remove(arr[nx][ny])


n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
alpha = set()
alpha.add(arr[0][0])

ans = 0
dfs(0,0,1)
print(ans)