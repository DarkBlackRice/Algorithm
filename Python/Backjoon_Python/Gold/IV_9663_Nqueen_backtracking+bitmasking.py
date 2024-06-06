# N-Queen 비트마스킹 while로 재귀구현


N = int(input())
count = 0
k, v1, v2, v3 = 0, 0, 0, 0
stack = [(k, v1, v2, v3)]
while stack:
    k, v1, v2, v3 = stack.pop()
    if k == N:
        count += 1

    for i in range(N):
        if (v1 & (1<<i) == 0) and (v2 & (1<<N-1+(k-i)) == 0) and \
            (v3 & (1<<k+i) == 0):
            # 비트마스킹 하기
            nv1 = v1 | (1<<i)
            nv2 = v2 | (1<<N-1+(k-i))
            nv3 = v3 | (1<<k+i)
            stack.append((k+1, nv1, nv2, nv3))

print(count)
