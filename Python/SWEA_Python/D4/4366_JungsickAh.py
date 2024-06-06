# 정식이의 은행업무

def check():
    for i in range(tri_len):
        back_up = tri_data[i]
        for _ in range(1, 3):
            temp = (int(tri_data[i]) + 1) % 3
            tri_data[i] = str(temp)
            temp_ans = int(''.join(tri_data), 3)
            if temp_ans in bin_arr:
                return temp_ans
        tri_data[i] = back_up


T = int(input())
for t in range(T):
    bin_data = input()
    bin_len = len(bin_data)
    bin_data = int(bin_data, 2)

    tri_data = list(input())
    tri_len = len(tri_data)

    bin_arr = []
    for i in range(bin_len):
        bin_arr.append(bin_data ^ (1 << i))

    print(f'#{t+1} {check()}')
