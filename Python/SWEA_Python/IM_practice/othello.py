# 재미있는 오셀로 게임

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = 2
    for m in range(M):
        sr, sc, color = map(int,input().split())
        sr -= 1
        sc -= 1
        board[sr][sc] = color
        other_color = 2//color
        for i in range(8):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if (0 <= nr < N) and (0 <= nc < N) and\
                (board[nr][nc] == other_color):
                temp = []
                r, c = nr, nc
                while (0 <= r < N) and (0 <= c < N) and\
                    (board[r][c] == other_color):
                    temp.append((r,c))
                    r += dr[i]
                    c += dc[i]
                if (0 <= r < N) and (0 <= c < N) and\
                    (board[r][c] == color):
                    for i, j in temp:
                        board[i][j] = color

    b_cnt, w_cnt = 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                b_cnt += 1
            elif board[r][c] == 2:
                w_cnt += 1
    
    print(f'#{t+1} {b_cnt} {w_cnt}')