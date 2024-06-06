# 종이 붙이기

T = int(input())

for t in range(T):
    N = int(input()) // 10

    f = [0] * 50
    f[0] = 1
    f[1] = 1
    for n in range(2,N+1):
        f[n] = f[n-2] + 2**(n-1)

    print(f'#{t+1} {f[N]}')