# 간단한 N 의 약수

N = int(input())

for n in range(1,N+1):
    if not N%n :
        print(n, end = ' ')