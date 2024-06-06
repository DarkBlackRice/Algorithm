# N 과 M (7)

def perm(k, lst):
    if k == M:
        print(*lst)
        return
    
    for i in range(N):
        perm(k+1, lst+[arr[i]])


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
perm(0, [])