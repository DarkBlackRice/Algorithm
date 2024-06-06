'''
랜덤 데이터 만들어보자
20까지 전부!

10
4 15
19 20
2 8
1 16
3 10
11 13
6 7
14 18
5 9
12 17

'''


# 자기 방으로 돌아가기

T = int(input())
for t in range(T):
    N = int(input())
    counting = [0]*201
    for _ in range(N):
        r1, r2 = map(lambda x : (int(x)+1)//2 ,input().split())
        s, e = min(r1, r2), max(r1, r2)
        for n in range(s, e+1):
            counting[n] += 1
    # print(counting[:15])
    print(f'#{t+1} {max(counting)}')