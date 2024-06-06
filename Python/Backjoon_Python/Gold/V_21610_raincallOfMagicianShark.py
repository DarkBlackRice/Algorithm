import sys; input = sys.stdin.readline
# 마법사 상어와 비바라기

dr1 = [0,-1,-1,-1,0,1,1,1]
dc1 = [-1,-1,0,1,1,1,0,-1]
dr2 = [-1,-1,1,1]
dc2 = [-1,1,-1,1]


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
clouded = [[0]*N for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1),(N-2, 0), (N-2, 1)]

for m in range(1, M+1):
    d, s = map(int, input().split())
    n_clouds = []
    for cloud in clouds:
        r, c = cloud
        nr = (r + dr1[d-1]*s) % N
        nc = (c + dc1[d-1]*s) % N
        clouded[nr][nc] = m
        arr[nr][nc] += 1
        n_clouds.append((nr,nc))
    for nr, nc in n_clouds:
        for i in range(4):
            nnr = nr + dr2[i]
            nnc = nc + dc2[i]
            if (0<=nnr<N) and (0<=nnc<N) and (arr[nnr][nnc]):
                arr[nr][nc] += 1

    clouds = []
    for r in range(N):
        for c in range(N):
            if arr[r][c]>=2 and clouded[r][c] != m:
                arr[r][c] -= 2
                clouds.append((r,c))

# 마지막 이동이면 물의 양 확인
water = 0
for r in range(N):
    for c in range(N):
        water += arr[r][c]

print(water)
