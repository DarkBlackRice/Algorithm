# 반사경

dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    r, c = 0, 0
    direction = 0
    count = 0
    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]
        if (nr < 0 or nr >= N) or (nc < 0 or nc >= N):
            break
        temp = board[nr][nc]
        if temp:
            count += 1
            if temp == 1:
                direction = 3 - direction
            else:
                if direction % 2:
                    direction -= 1
                else:
                    direction += 1
        r = nr
        c = nc
    print(f'#{t+1} {count}')