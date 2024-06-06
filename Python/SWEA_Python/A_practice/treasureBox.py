# 보물상자 비밀번호

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    data = list(map(lambda x: int(x, 16), input()))
    rotate = N//4
    ans = []
    for _ in range(rotate):
        i = 0
        while i < N:
            num = 0
            for j in range(rotate):
                num = num*16 + data[i+j]
            if num not in ans:
                ans.append(num)
            i += rotate
        data = [data.pop()] + data
    ans.sort()
    print(f'#{t+1} {ans[::-1][K-1]}')
