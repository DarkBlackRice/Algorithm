# N 과 M (8)

def perm(k, lst, m):
    if k == M:
        print(*lst)
        return
    
    for i in range(m, N):
        perm(k+1, lst+[arr[i]], i)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
perm(0, [], 0)