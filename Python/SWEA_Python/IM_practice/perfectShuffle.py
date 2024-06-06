# 퍼펙트 셔플

T = int(input())
for t in range(T):
    length = int(input())
    cards = list(input().split())
    lst = []
    for i in range(length):
        if i%2:
            lst.append((length+i)//2)
        else:
            lst.append(i//2)

    print(f'#{t+1}', end=' ')
    for index in lst:
        print(cards[index], end=' ')
    print()