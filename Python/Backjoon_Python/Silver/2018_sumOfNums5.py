# 수들의 합 5

N = int(input())

i = 0
cursum = j = cnt = 1

while i < N and j < N:
    if cursum < N:
        j += 1
        cursum += j
    else:
        if cursum == N:
            cnt += 1
        i += 1
        cursum -= i

print(cnt)