# 뒤집기 2

def flip(row, col):
    for r in range(row + 1):
        for c in range(col + 1):
            arr[r][c] ^= 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = 0

# 반대각선 하단
for i in range(M):
    length = min(N, i+1)
    for j in range(length):
        if arr[N-1-j][M-1-i+j] == 1:
            ans += 1
            flip(N-1-j, M-1-i+j)

# 반대각선 상단
for i in range(N):
    length = min(N-i, M)
    for j in range(length):
        if arr[N-1-i-j][j] == 1:
            ans += 1
            flip(N-1-i-j, j)
print(ans)
