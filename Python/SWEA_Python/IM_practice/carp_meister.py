# 진기의 최고급 붕어빵

def carp_mapping():
    last = 0
    for i in range(max_time):
        for _ in range(cnt_lst[i]):
            if carp_lst[last] > i:
                return 'Impossible'
            last += 1
    return 'Possible'


T = int(input())
for t in range(T):
    max_time = 11120
    cnt_lst = [0] * max_time
    N, M, K = map(int,input().split())
    
    time_data = list(map(int,input().split()))
    for ti in time_data:
        cnt_lst[ti] += 1
    
    carp_lst = []
    for i in range(1, N//K + 2):
        carp_lst += [M*i] * K
    
    print(f'#{t+1} {carp_mapping()}')