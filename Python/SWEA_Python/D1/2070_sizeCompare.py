# 큰 놈, 작은 놈, 같은 놈

T = int(input())

for t in range(1,T+1):
    num = list(map(int,input().split()))
    result = ''
    if num[0]<num[1]:
        result = '<'
    elif num[0]>num[1]:
        result = '>'
    else:
        result = '='

    print(f"#{t} {result}")