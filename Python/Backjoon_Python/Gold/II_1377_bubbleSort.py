# 버블 소트

N = int(input())
arr = []
for i in range(N):
    arr.append((int(input()), i))

arr.sort()
max_v = 0
for i in range(N):
    tmp = arr[i][1] - i
    if max_v < tmp:
        max_v = tmp

print(max_v + 1)