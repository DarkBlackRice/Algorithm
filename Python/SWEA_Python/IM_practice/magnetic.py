# magnetic

import sys; sys.stdin = open('magnetic_input.txt')

T = 10
for t in range(T):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for c in range(N):
        n_toggle = False
        for r in range(N):
            if n_toggle:
                if board[r][c] == 2:
                    count+=1
                    n_toggle = False
            else:
                if board[r][c] == 1:
                    n_toggle = True
    print(f'#{t+1} {count}')