# 백만장자 프로젝트

import sys; sys.stdin = open('1859_input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    start = 0
    total_price = 0
    while start < N-1:
        max_price_idx = start
        for i in range(start, N):
            if price[max_price_idx] < price[i]:
                max_price_idx = i
        
        
        for i in range(start, max_price_idx):
            total_price += price[max_price_idx] - price[i]

        start = max_price_idx + 1
    print(f'#{t+1} {total_price}')