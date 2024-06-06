# 벽돌 깨기
import copy

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def pi(n, lst):
    if n == N:
        ball_list.append(lst)
        return
    for i in range(W):
        pi(n+1, lst+[i])


T = int(input())
for t in range(T):
    N, W, H = map(int,input().split())
    ref_arr = [list(map(int,input().split())) for _ in range(H)]

    # 만약 게임보드의 값이 모두 1 초과로 차있다면, 어딜 건드리든 0 -> 이거 하지말고 그냥 답 0으로 줍시다
    
    ball_list = []
    min_v = 0

    is_valid = False
    for r in range(H):
        for c in range(W):
            if ref_arr[r][c] < 2:
                is_valid = True
                break
    if is_valid:
        min_v = 300
        pi(0,[])

    

    for case in ball_list:  # 공 위치의 모든 경우의 수 중 하나를 가져오자
    # for case in [[2,2,6]]:
        
        arr = copy.deepcopy(ref_arr)
        for c1 in case: # 해당 케이스의 해당 순서 위치에 대해서 N번 반복

            stack = []
            for r1 in range(H): # 최초로 공을 떨어뜨리자
                if arr[r1][c1] != 0:    #최초로 0이 아닌 경우를 발견했다면 
                    stack.append((r1, c1, arr[r1][c1])) # stack에 넣으세요
                    arr[r1][c1] = 0                     # 그리고 터뜨려
                    break
            
            # 터뜨리기
            while stack:
                row, col, radius = stack.pop()
                for ra in range(1, radius):
                    for i in range(4):
                        nr = row + dr[i]*ra
                        nc = col + dc[i]*ra
                        if 0<=nr<H and 0<=nc<W:
                            if not arr[nr][nc]:
                                continue
                            if arr[nr][nc] > 1:
                                stack.append((nr,nc,arr[nr][nc]))
                            arr[nr][nc] = 0

            # 벽돌 내리기
            for col2 in range(W):
                zero_cnt = 0    
                for row2 in range(H-1, -1, -1):
                    if not arr[row2][col2]:
                        zero_cnt += 1
                    else:
                        if zero_cnt:
                            arr[row2+zero_cnt][col2] = arr[row2][col2]
                            arr[row2][col2] = 0
                        

        cnt = 0
        for r2 in range(H):
            for c2 in range(W):
                if arr[r2][c2] != 0:
                    cnt += 1
        if min_v > cnt:
            min_v = cnt

    print(f'#{t+1} {min_v}')