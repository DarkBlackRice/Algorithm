# N 과 M (9)

def perm(k, lst):
    if k == M:
        print(*lst)
        return
    
    rem = 0
    for i in range(N):
        if not v[i] and arr[i] != rem:
            rem = arr[i]
            v[i] = 1
            perm(k+1, lst+[arr[i]])
            v[i] = 0


N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
v = [0] * N
perm(0, [])