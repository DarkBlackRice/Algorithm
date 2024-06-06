# 카드 2
from collections import deque

N = int(input())
q = deque(list(range(1,N+1)))
for _ in range(N-1):
    q.popleft()
    q.append(q.popleft())
print(q.pop())