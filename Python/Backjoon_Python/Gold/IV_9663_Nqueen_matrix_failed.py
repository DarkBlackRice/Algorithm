# N-Queen 2트

def dfs(k, n, view):
    global count

    # 완성했다면 세어라.
    if k == n:
        # print(count+1)
        # for c in view:
        #     print(*c)
        count += 1
        return
    
    # 가망이 없다면 그만 돌아라.
    for rev_r in range(n-1, k-1, -1):
        if 0 not in view[rev_r]:
            return

    for i in range(n):
        if not view[k][i]:
            view[k][i] = '*'
            check_lst = []
            for j in range(1,n-k):
                for d in [-1,0,1]:
                    nc = i + d*j
                    if (0 <= nc < N) and (not view[k+j][nc]):
                        view[k+j][nc] = 1
                        check_lst.append((k+j,nc))
            dfs(k+1, n, view)
            view[k][i] = 0
            for coord in check_lst:
                r, c = coord
                view[r][c] = 0

N = int(input())
check = [[0]*N for _ in range(N)]
count = 0
dfs(0,N,check)
print(count)