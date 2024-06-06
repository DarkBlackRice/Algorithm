# 잃어버린 괄호

# 전략 : + 우선연산

def cal(n1, n2, op):
    if op == '+':
        return n1+n2
    else:
        return n1-n2


data = list(input())
N = len(data)
tmp = []
arr = []
for i in range(N):
    if data[i].isdigit():
        tmp.append(data[i])
    else:
        arr.append(''.join(tmp))
        tmp = []
        arr.append(data[i])
        
arr.append(''.join(tmp))

postfix = []
stack = []
for a in arr:
    if a.isdigit():
        postfix.append(a)
    else:
        if a == '+':
            stack.append(a)
        else:
            while stack:
                postfix.append(stack.pop())
            stack.append(a)
while stack:
    postfix.append(stack.pop())

for p in postfix:
    if p.isdigit():
        stack.append(int(p))
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(cal(n1,n2,p))

print(stack.pop())
