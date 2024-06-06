#연월일 달력

T = int(input())

for t in range(T):
    data = input()

    year = int(data[:4])
    month = int(data[4:6])
    day = int(data[6:])
    is_correct = ((month in [1,3,5,7,8,10,12] and day in range(1,32))
                or (month in [4,6,9,11] and day in range(1,31))
                or (month == 2 and day in range(1,29))
    )

    if is_correct:
        print("#%d %04d/%02d/%02d"%(t+1,year,month,day))

    else:
        print(f"#{t+1} -1")