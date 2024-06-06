# 평균값 구하기

T = int(input())

for t in range(1,T+1):
    nums = list(map(int,input().split()))
    sum = 0
    for num in nums:
        sum += num

    print(f"#{t} {int(round(sum/10,0))}")