# 스택 수열

N = int(input())
stack = []
result = []
num = 1
for i in range(N):
    input_num = int(input())
    if num <= input_num:
        while num <= input_num:
            stack.append(num)
            result.append('+')
            num += 1
        stack.pop()
        result.append('-')
    else:
        tmp = stack.pop()
        result.append('-')
        if tmp != input_num:
            print('NO')
            quit(0)
for r in result:
    print(r)