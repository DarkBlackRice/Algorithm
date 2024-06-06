# 팩토리얼 2

def fact(num):
    if num > 1:
        return num * fact(num-1)
    else:
        return 1
    
N = int(input())
print(fact(N))