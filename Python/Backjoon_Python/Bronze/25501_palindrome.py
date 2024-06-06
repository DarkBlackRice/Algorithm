# 재귀의 귀재

def pel(string):
    global count
    count += 1

    if len(string) <= 1:
        return 1
    elif string[0] != string[-1]:
        return 0
    else:
        return pel(string[1:-1])

T = int(input())

for t in range(1,T+1):
    S = input()
    count = 0

    print(pel(S), count)
