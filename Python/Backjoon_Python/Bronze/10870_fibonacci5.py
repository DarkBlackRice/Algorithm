# 피보나치 5

def fibo(num):

    if num > 2:
        return fibo(num-1) + fibo(num-2)
    elif num == 0:
        return 0
    else :
        return 1

N = int(input())
print(fibo(N))