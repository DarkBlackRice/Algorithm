# 숨바꼭질

from collections import deque

def bfs(k):
    q = deque([k])
    vst[k] = 1
    while q:
        v = q.popleft()
        if v == K:
            return vst[v] - 1 
        for w in [v*2, v-1, v+1]:
            if 0 <= w <= 200_000 and not vst[w]:
                vst[w] = vst[v] + 1
                q.append(w)

N, K = map(int, input().split())
vst = [0] * 200_001
print(bfs(N))