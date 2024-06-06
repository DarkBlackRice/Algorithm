# N-Queen 3트

def dfs(k):
    global count
    if k == N:
        count += 1
        return

    for i in range(N):        
        if v1[i] == v2[N-1 + (k-i)] == v3[k+i] == 0: 
            v1[i] = v2[N-1 + (k-i)] = v3[k+i] = 1
            dfs(k+1)
            v1[i] = v2[N-1 + (k-i)] = v3[k+i] = 0

N = int(input())
# 다음 배열은 퀸의 유망한 좌표를 가지치기하기 위해 쓰인다
v1 = [0] * N        # 같은 열에 퀸이 이미 있는가?
v2 = [0] * 2 * N    # 같은 주대각선에 퀸이 이미 있는가? : 행-열이 일치하면 이미 존재
v3 = [0] * 2 * N    # 같은 반대각선에 퀸이 이미 있는가? : 행+열이 일치하면 이미 존재

count = 0
dfs(0)
print(count)