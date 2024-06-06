# 설탕 배달

ref_lst = [0,-1,-1,1,-1,1] # 1~5까지 사용 가능한 정수만 1 아니면 -1

N = int(input())

for n in range(6,N+1):

    min_v = 0xffffff
    for i in [num for num in ref_lst if num > 0]:
        if ref_lst[i] != -1 and ref_lst[n-i] != -1:
            temp = ref_lst[i] + ref_lst[n-i]
            if min_v > temp:
                min_v = temp

    if min_v != 0xffffff:
        ref_lst.append(min_v)
    else:
        ref_lst.append(-1)

print(ref_lst[N])
