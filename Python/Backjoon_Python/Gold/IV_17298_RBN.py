# 오(른쪽)큰 수

N = int(input())
arr = list(map(int, input().split()))
stack = [arr[N-1]]
result = [-1]
for i in range(N-2,-1,-1):
    num = arr[i]
    while stack and stack[-1] <= num:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)
    stack.append(num)
        
result.reverse()
print(*result)