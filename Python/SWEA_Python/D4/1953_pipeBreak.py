# 탈주범 검거
import sys; sys.stdin = open('1953_input.txt')
from collections import deque

# 델타의 방향은 우, 하, 좌, 상 순서이다.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 진입방향에 따라 진입할 수 있는 파이프가 다르다.
# 다음은 해당 데이터를 리스트로 묶어놓은 것이다.
# ex) 델타의 0번 방향은 우 방향이다. 이 때 진입할 수 있는 파이프는
# 1번(+형) 3번(-형) 6번(ㄱ형) 7번(뒤집은 ㄴ형) 뿐이다. 나머지는 진입할 수 없다.
into = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]

# 현재 파이프의 데이터에 따라 진출할 수 있는 방향이 다르다.
# 다음은 해당 데이터를 리스트로 묶어놓은 것이다.
# ex) 0은 파이프가 없으므로 진출할 수 있는 방향이 없다.
# ex) 1은 +형 파이프로 전 방향으로 진출할 수 있다.
# ex) 4번은 ㄴ형 파이프로 우(0번 방향) 상(3번 방향)으로 진출할 수 있다.
outto = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]


def bfs():
    row, col = R, C
    q = deque([(row, col)])
    v[row][col] = 1
    # 맨홀뚜껑에 계속 머물러 있을 수도 있다 cnt는 1부터 시작이다.
    cnt = 1
    while q:
        r, c = q.popleft()
        # 만약 탐색깊이가 L 이상이 되면 탐색을 중지한다.
        if v[r][c] == L:
            break
        # pipeline에서 현재좌표 r,c 에 대한 정보를 받아와서 outto 리스트를 참조한다.
        for i in outto[pipeline[r][c]]:
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and \
                (not v[nr][nc]):
                # 다음 과정을 통해서 i 방향으로 들어왔을 때,
                # pipeline[nr][nc]로 진출할 수 있는지 판단한다.
                # 파이썬에서는 간단하게 in을 사용해도 된다.
                for j in into[i]:
                    if pipeline[nr][nc] == j:
                        # 방문처리 하면서 동시에 cnt를 증가시켜준다
                        cnt += 1
                        v[nr][nc] = v[r][c] + 1
                        q.append((nr, nc))
                        break   # for j를 탈출하여 for i 라인으로 이동한다.

    # 방문한 파이프의 수를 return 한다.
    return cnt


T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    pipeline = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    print(f'#{t + 1} {bfs()}')
