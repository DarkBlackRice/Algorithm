# 몫과 나머지 출력하기

T = int(input())

for t in range(1,T+1):
    a, b = map(int,input().split())
    print(f"#{t} {a//b} {a%b}")