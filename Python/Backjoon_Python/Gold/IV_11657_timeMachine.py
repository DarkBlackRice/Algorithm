# 타임머신
from heapq import heappop, heappush

def bellman_ford(n):
    pq = []
    distance[n] = 0
    heappush(pq, (distance[n], n))
    cnt = 0
    while pq:
        if cnt == N-1:
            return False

        vw, v = heappop(pq)
        cnt += 1
        for u in range(N+1):
            if graph[v][u] and distance[u] > graph[v][u] + vw:
                distance[u] = graph[v][u] + vw
                heappush(pq, (distance[u], u))

    return True

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
distance = [1e12] * (N+1)
for _ in range(M):
    s, e, w = map(int, input().split())
    if not graph[s][e] or graph[s][e] > w:
        graph[s][e] = w

if bellman_ford(1):
    for i in range(2, N+1):
        if distance[i] == 1e12:
            print(-1)
        else:
            print(distance[i])

else:
    print(-1)
