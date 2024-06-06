# 칸토어 집합

def cantor_line(num):
    if num >= 1:
        blank = ' ' * (3**(num-1))
        return cantor_line(num-1) + blank + cantor_line(num-1)
    else:
        return '-'


while True :
    try:
        N = int(input())
        print(cantor_line(N))

    except:
        break