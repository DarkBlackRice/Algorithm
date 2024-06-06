# Z

def z(k, sr, sc, tr, tc, cnt):
    if k == 0:
        return cnt
    
    tmp = 0
    if sr + 2**(k-1) <= tr:
        sr += 2**(k-1)
        tmp += 2
    if sc + 2**(k-1) <= tc:
        sc += 2**(k-1)
        tmp += 1
    return z(k-1, sr, sc, tr, tc, cnt*4 + tmp)
 

N, r, c = map(int, input().split())
print(f'{z(N, 0, 0, r, c, 0)}')
