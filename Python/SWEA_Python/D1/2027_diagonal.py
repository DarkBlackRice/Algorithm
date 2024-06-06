# 대각선 출력하기

repeatNum = 5

for i in range(5):
    plus_list = ['+']*repeatNum
    plus_list[i] = '#'
    print(''.join(plus_list))