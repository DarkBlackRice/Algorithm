# 정곤이의 단조증가하는 수

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    lst = []
    ans = []
    for i in range(0,N-1):
        for j in range(i+1,N):
            # print(f'현재의 i, j 조합 : {i}, {j} \n 따라서 {arr[i]} * {arr[j]} 인 {arr[i]*arr[j]}가 lst에 들어간다')
            lst.append(arr[i]*arr[j])
    # print(lst)

    for num in lst:
        temp = num
        last = 10
        flag = True
        while temp:
            n = temp % 10
            temp //= 10
            if n > last:
                flag = False
                break
            last = n
        if flag:
            ans.append(num)
    # print(ans)
    
    
    max_v = -1
    for a in ans:
        if max_v < a:
            max_v = a

    print(f'#{t+1} {max_v}')