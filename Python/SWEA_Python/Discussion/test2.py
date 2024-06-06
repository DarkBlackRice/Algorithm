# 백준 1987 알파벳 : 레퍼런스 코드 참고하여 새로 짜기

delta = [[-1,0],[1,0],[0,-1],[0,1]]

N, M = map(int,input().split())
arr = [list(input().split()) for _ in range(N)]
sx, sy = 0, 0
ans = 0
stack = [(sx,sy,1)]
alpha = [0] * 26
alpha[ord(arr[sx][sy]) - 65] = 1
while stack:
    x, y , cnt = stack.pop()
    ans = max(ans, cnt)
    if ans == 26:
        break
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N) and (0 <= ny < M) and\
            not alpha[ord(arr[nx][ny]) - 65]:
            alpha[ord(arr[nx][ny]) - 65] = 1
            


