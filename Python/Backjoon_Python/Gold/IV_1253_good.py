# 좋다

# 놓친 부분
# 1. 데이터를 자연수로 상정함
# 결론 : 문제 잘 읽어라 지환아 제발

N = int(input())
arr = sorted(list(map(int, input().split())))

cnt = 0
for i in range(N):
    j = 0
    k = N - 1
    tg = arr[i]
    while j < k:
        tmp = arr[j] + arr[k]
        if tg == tmp:
            # i번째 수는 "i번째가 아닌" 다른 위치의 두 수로 만들어져야 함!
            if j != i and k != i:
                cnt += 1
                break
            # 만약 작은 포인터 쪽의 위치가 i와 같다면 작은 포인터를 키워서 탈출
            elif j == i:
                j += 1
            # 반대라면 큰 포인터를 낮춰서 탈출
            else:
                k -= 1

        elif tg > tmp:
            j += 1

        else:
            k -= 1

print(cnt)