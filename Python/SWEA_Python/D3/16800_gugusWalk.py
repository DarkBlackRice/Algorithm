# 구구단 걷기
import math

TC = int(input())

for t in range(1,1+TC):
    num = int(input())

    max_div = 0
    for n in range(1,int(math.sqrt(num))+1):
        if not (num % n):
            if max_div < n:
                max_div = n
    
    print(f'#{t} {(max_div - 1) + (num//max_div - 1)}')
