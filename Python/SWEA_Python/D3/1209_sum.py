# S/W 문제해결 기본 : 2일차 - Sum

import sys; sys.stdin = open('1209_input.txt')

for t in range(10):
    tc = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]

    max_v = 0
    f_dig_sum = 0
    r_dig_sum = 0
    for r in range(100):
    
        f_dig_sum += board[r][r]
        r_dig_sum += board[r][99-r]
        
        row_sum = col_sum = 0

        for c in range(100):

            row_sum += board[r][c]
            col_sum += board[c][r]
            
            # 최댓값 구하기
        if max_v < row_sum:
            max_v = row_sum
        if max_v < col_sum:
            max_v = col_sum
    if max_v < r_dig_sum:
        max_v = r_dig_sum
    if max_v < f_dig_sum:
        max_v = f_dig_sum

    print(f'#{tc} {max_v}')
