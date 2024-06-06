# 물놀이를 가자
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs():
    # 이미 W 좌표가 q 에 다 들어가 있기 때문에 시작좌표를 설정해줄 필요는 없다
    # 단 cnt 에 거리(깊이)를 저장하기 위해서 선언해줌
    cnt = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and v[nr][nc] == -1:
                v[nr][nc] = v[r][c] + 1
                # 한 번 방문한 좌표는 다시 방문하지 않기 때문에
                # 방문처리할 때 저장된 깊이를 cnt 에 더해줘도 중복되지 않음
                cnt += v[nr][nc]
                q.append((nr, nc))
    return cnt


T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    # W가 있는 곳은 깊이가 0이 되어야 하므로 -1로 초기값 설정
    v = [[-1] * M for _ in range(N)]

    # arr 을 한 줄씩 받아서 append 해줄 예정이므로 빈리스트로 선언
    arr = []

    # 밖에서 queue 에 W 좌표를 enqueue 해줘야 하므로 함수 밖에 선언
    q = deque([])

    # W가 있는 좌표를 q 에 넣어주면서 맵을 받읍시다.
    for row in range(N):
        temp = list(input())
        arr.append(temp)
        for col in range(M):
            if temp[col] == 'W':
                v[row][col] = 0
                q.append((row, col))

    print(f'#{t+1} {bfs()}')

