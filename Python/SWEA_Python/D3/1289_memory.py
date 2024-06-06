# 원재의 메모리 복구하기

T = int(input())

for t in range(T):
    index = 0
    restore = input()
    flag = '0'
    count = 0

    while index < len(restore):
        if flag == restore[index] :
            index+=1
        else:
            flag = restore[index]
            count +=1
            index +=1
            

    print(f"#{t+1} {count}")