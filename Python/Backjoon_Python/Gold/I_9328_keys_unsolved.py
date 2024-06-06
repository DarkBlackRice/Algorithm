# 열쇠

from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(row, col):
    global ans
    q = deque([(row, col)])
    visited[row][col] = v_count
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < h) and (0 <= nc < w)\
                and room_map[nr][nc] != '*'\
                and not (65 <= ord(room_map[nr][nc]) <= 90)\
                and visited[nr][nc] != v_count:
                q.append((nr, nc))
                visited[nr][nc] = v_count
                if 97 <= ord(room_map[nr][nc]) <= 122:
                    key_set.add(room_map[nr][nc])
                    room_map[nr][nc] = '.'
                elif room_map[nr][nc] == '$':
                    ans += 1
                    room_map[nr][nc] = '.'



T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    room_map = [list(input()) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if room_map[r][c] == '.':
                visited[r][c] = 0

    v_count = 0
    ans = 0

    key_set = set(input())
    
    while key_set:
        key_list = list(key_set)
        for key in key_list:
            key_ord = ord(key)
            for r in range(h):
                for c in range(w):
                    if ord(room_map[r][c]) == key_ord - 32:
                        room_map[r][c] = '.'
        key_set = set()
        v_count += 1

        # 둘레를 따라 침입할 수 있다.
        # 침입 시, '.' 뿐 아니라 열쇠와 $를 통해서 또한 가능하다는 걸 반영하자.
        for r in range(h):
            if visited[r][0] != -1 and visited[r][0] != v_count:
                    bfs(r, 0)
            elif visited[r][w-1] != -1 and visited[r][w-1] != v_count:
                    bfs(r, w-1)
        for c in range(1, w-1):
            if visited[0][c] != -1 and visited[0][c] != v_count:
                    bfs(0, c)
            elif visited[h-1][c] != -1 and visited[h-1][c] != v_count:
                    bfs(h-1, c)
            
    print(ans)