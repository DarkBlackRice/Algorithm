# 트리의 지름
from collections import deque

# 다음 노드와 가중치를 q에 튜플로 묶어 넣어 관리하자
def bfs(n):
    global ans
    q = deque([n])
    vst[n] = 0
    while q:
        v = q.popleft()
        for w, weight in graph[v]:
            if vst[w] == -1:
                vst[w] = vst[v] + weight
                q.append(w)


N = int(input())

# 그래프 만들기
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    arr = list(map(int, input().split()))
    j = 1
    while arr[j] != -1:
        # 0번 원소는 도착노드, 1번 원소는 가중치
        arrived, weight = arr[j], arr[j+1]
        # 바보냐 ㅋㅋㅋㅋ 노드가 순서대로 안 들어올 수도 있자너!!
        graph[arr[0]].append((arrived, weight))
        j += 2

# 전체 노드를 대상으로 bfs탐색을 하자. <-- 이거 안 쓸거임 ㅋㅋ
ans = 0
node1 = 0
vst = [-1] * (N+1)

# 지름 구하는 알고리즘 : 
# 임의의 점에서 가장 먼 점이 1번 지름노드가 되고,
# 1번 지름노드에서 가장 거리가 먼 노드가 2번 지름노드, 해당 거리가 지름이 된다.
bfs(1)
for i in range(1, N+1):
    if ans < vst[i]:
        node1 = i
        ans = vst[i]

vst = [-1] * (N+1)
bfs(node1)
print(max(vst))