# 절댓값 힙
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

pq = []
N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp:
        heappush(pq, (abs(tmp), tmp//abs(tmp)))
    else:
        if pq:
            num, sign = heappop(pq)
            print(num * sign)
        else:
            print(0)
