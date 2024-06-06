# 빙산
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(row, col):

    global iceberg_size
    measured_size = 1
    q = deque([(row, col)])
    visited[row][col] = year

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and\
                visited[nr][nc] != year:
                if iceberg[nr][nc]:         # 4방탐색에서 빙산이 나오면
                    measured_size += 1      # 실측 크기를 1 증가시켜라.
                    q.append((nr,nc))       # 탐색할 좌표를 큐에 넣고
                    visited[nr][nc] = year  # year 데이터로 방문처리,
                                            # (매 번 새 visited를 만들지 않기 위함)

                elif iceberg[r][c]:         # 4방탐색에서 바다가 나오고, 현재 방문 빙산의 크기가 있다면,
                    iceberg[r][c] -= 1      # 빙산의 값을 하나 깎고
                    if not iceberg[r][c]:   # 방금의 연산으로 0이 되었다면,
                        iceberg_size -= 1   # 빙산 크기를 1 깎아라.
                        measured_size -= 1  # 실측 크기도 1 깎아라.
                        # 이렇게 하면 정상적으로 탐색이 완료되었을 때,
                        # 1년이 흐른 시기 기준의 빙산맵의 크기가 실측 크기와 빙산 크기에 저장된다.
                        # 일치하면 *전년도* 빙산이 부서지지 않은 것.
                        # 일치하지 않는다면, 실측 크기가 덜 쌓인 것, 즉 탐색할 수 없는 장소가 있다는 것.
                        # 즉, 전년도에 빙산이 부서졌다는 것.
    return iceberg_size == measured_size


def explore():
    for r in range(1, N-1):
        for c in range(1, M-1):
            if iceberg[r][c]:
                return bfs(r,c)


N, M = map(int,input().split())
iceberg = []
visited = []
iceberg_size = 0
for r in range(N):
    temp = list(map(int,input().split()))
    iceberg.append(temp)
    visited.append([0]*M)
    for c in range(M):
        if temp[c]:
            iceberg_size += 1

ice_break = False
year = 0
while iceberg_size :
    year += 1
    if not explore():
        ice_break = True
        break
    
if ice_break:
    print(year-1)
else:
    print(0)