# 재귀 비트마스킹 : 매개변수로 전달

# def dfs(k, v1, v2, v3):
#     global count
#     if k == N:
#         count += 1
#         return

#     for i in range(N):
#         if (v1 & (1<<i) == 0) and (v2 & (1<<N-1+(k-i)) == 0) and \
#             (v3 & (1<<k+i) == 0):
#             # 비트마스킹 하기
#             nv1 = v1 | (1<<i)
#             nv2 = v2 | (1<<N-1+(k-i))
#             nv3 = v3 | (1<<k+i)
#             dfs(k+1, nv1, nv2, nv3)

# N = int(input())
# count = 0
# dfs(0, 0, 0, 0)
# print(count)


# 재귀 비트마스킹 : 전역변수

def dfs(k):
    global count, v1, v2, v3
    if k == N:
        count += 1
        return

    for i in range(N):
        if (v1 & (1<<i) == 0) and (v2 & (1<<N-1+(k-i)) == 0) and \
            (v3 & (1<<k+i) == 0):
            # 비트마스킹 하기
            v1 = v1 | (1<<i)
            v2 = v2 | (1<<N-1+(k-i))
            v3 = v3 | (1<<k+i)
            dfs(k+1)
            v1 = v1 & ~(1<<i)
            v2 = v2 & ~(1<<N-1+(k-i))
            v3 = v3 & ~(1<<k+i)

N = int(input())
count, v1, v2, v3 = 0, 0, 0, 0
dfs(0)
print(count)