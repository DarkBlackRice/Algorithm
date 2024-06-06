N = int(input())

for num in map(str,range(1,N+1)):
    if ('3' in num) or ('6' in num) or ('9' in num):
        times=num.count('3')+num.count('6')+num.count('9')
        for i in range(times):
            print('-',end='')
        print('',end=' ')
    else:
        print(num,end=' ')