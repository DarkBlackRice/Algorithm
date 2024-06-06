# 오목판정

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def judge(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for i in range(8):
                    count = 0
                    for m in range(1,5):
                        nr = r + dr[i]*m
                        nc = c + dc[i]*m
                        if (0<=nr<N) and (0<=nc<N) and\
                            arr[nr][nc]=='o':
                            count += 1
                        else:
                            break
                    if count == 4:
                        return 'YES'
    return 'NO'


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    print(f'#{t+1} {judge(board)}')