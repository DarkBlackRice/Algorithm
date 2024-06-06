# 쇠막대기 자르기

T = int(input())

for t in range(T):
    data = input()
    stack = []
    count = 0
    for i in data:
        if i == '(':
            laser = True
            stack.append(i)
        elif stack and i == ')':
            stack.pop()
            if laser:
                laser = False
                count += len(stack)
            else:
                count += 1
    print(f'#{t+1} {count}')