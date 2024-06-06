# 토마토

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 큐 함수 구현부
def enqueue(data):
    global rear
    if rear == size - 1:
        print('Queue_Full')
        return
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    if front == rear:
        print('Queue_Empty')
        return
    front += 1
    return queue[front]


#bfs 함수부
def bfs(init_coord_lst):
    global front, rear
    # 시작좌표 queue에 입력
    for coord in init_coord_lst:
        enqueue(coord)
        
    # 본격적인 탐색
    while front < rear:
        
        r, c = dequeue()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M) and\
                (box[nr][nc] == 0):
                box[nr][nc] = box[r][c] + 1
                enqueue((nr, nc))


# 본 코드--------------------------------------------------
M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

# 시작점 찾기
st_point = []
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            st_point.append((r,c))

# 탐색
size = 2000000
queue = [()] * size
front = -1
rear = -1
count = 0
# visited = [[0]*M for _ in range(N)]
bfs(st_point)

# 안 익은 토마토가 있는지 검사
result = 1
max_date = 0
for r in range(N):
    for c in range(M):
        temp = box[r][c]
        if temp == 0:
            # print(f'당신의 토마토는 글렀습니다.')
            print(-1)
            exit(0)
        if max_date < temp:
            max_date = temp
        
# print()
# for b in box:
#     print(*b)
if max_date == 1:
    # print('이미 다 익었습니다. 결과 : 0')
    print(0)
else:
    # print(f'결과 : {max_date}일에 걸쳐 다 익습니다.')
    print(max_date - 1)