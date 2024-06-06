# 오목
import sys
input = sys.stdin.readline

is_winner = False


def src_board(r,c):

    global is_winner
    stone_color = board[r][c]

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        count = 1

        while 0 <= nr <= 18 and 0 <= nc <= 18 and board[nr][nc] == stone_color:
            count += 1

            if count == 5:
                if 0 <= r - dr[d] <= 18 and 0 <= c - dc[d] <= 18 and board[r - dr[d]][c - dc[d]] == stone_color:
                    break
                if 0 <= nr + dr[d] <= 18 and 0 <= nc + dc[d] <= 18 and board[nr + dr[d]][nc + dc[d]] == stone_color:
                    break
                print(stone_color)
                print(r+1,c+1)
                exit(0)

            nr += dr[d]
            nc += dc[d]

    return


board = [list(map(int,input().split())) for _ in range(19)]

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            src_board(i,j)

if not is_winner:
    print(0)

