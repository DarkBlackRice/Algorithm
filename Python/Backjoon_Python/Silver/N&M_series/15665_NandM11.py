# N 과 M (11)

def perm(k, lst, m):
    if k == M:
        print(*lst)
        return
    
    rem = 0
    for i in range(m, N):
        if arr[i] != rem:
            rem = arr[i]
            perm(k+1, lst+[arr[i]], i)


N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
perm(0, [], 0)