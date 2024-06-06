# RGB 거리
N = int(input())
cost_list = [list(map(int,input().split())) for _ in range(N)]
dp = cost_list[0]

for n in range(1, N):
    n_dp = []
    for i in range(3):
        # print(cost_list[n][i], dp[1 - i*(i%2)], dp[2 - i*((i+1)%2)]) 디버깅 프린트
        n_dp.append(cost_list[n][i] + min(dp[1 - i*(i%2)], dp[2 - i*((i+1)%2)]))
        # 새 dp 리스트에는 해당하는 n의 각 코스트의 인덱스별로
        # 구 dp 리스트의 "해당 인덱스가 아닌" 값들의 최솟값을 더해준다.
    dp = n_dp

print(min(dp))