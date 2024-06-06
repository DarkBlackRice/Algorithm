# 다리 놓기

def count_case(left, right):

    upper = lower = 1
    for i in range(right-left+1,right+1):
        upper *= i
    for i in range(1, left+1):        
        lower *= i
    
    return upper//lower


T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    
    print(count_case(N, M))

        