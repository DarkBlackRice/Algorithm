#길 찾기

import sys; sys.stdin = open('1219_input.txt')

def dfs(start, goal):
    vst[start] = 1
    for w in gragh[start]:
        if w == 99:
            global ans
            ans = 1
            return
        if not vst[w]:
            dfs(w, goal)
    return

T = 10
N = 100
S = 0
G = 99

for t in range(T):
    tc, E = map(int,input().split())
    data = list(map(int,input().split()))
    gragh = [[] for _ in range(N)]
    for i in range(E):
        gragh[data[2*i]].append(data[2*i+1])
    vst = [0] * 100
    ans = 0
    dfs(S, G)

    print(f'#{t+1} {ans}')