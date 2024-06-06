# 1대 1 가위바위보

a,b = map(int,input().split())

if 2 not in [a,b]:
    if a>b:
        print('B')
    else:
        print('A')
else:
    if a>b:
        print('A')
    else:
        print('B')

#이 쉬운 문제가 20분짜리라고..? 허허...
#걸린 시간 00:19:29