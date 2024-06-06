# N-Queen

def promising_lst(k,lst):

    if k < 1:
         return list(range(N))

    result = []
    for num in range(N):
        promising = True
        for i in range(1, k+1):
            for j in [-1, 0 ,1]:
                if num == lst[k-i] + j*i:
                    promising = False
                    break
            if not promising:
                break
        if promising:
            result.append(num)
    return result

def dfs(k, n, lst):
    global count
    if k == n:
        count += 1
        return

    for i in promising_lst(k, lst):        
        dfs(k+1, n, lst+[i])



N = int(input())
count = 0
dfs(0, N, [])
print(count)