# N 과 M (6)

def perm(k, lst, m):
    if k == M:
        print(*lst)
        return
    
    for i in range(m, N):
        perm(k+1, lst+[arr[i]], i+1)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
perm(0, [], 0)