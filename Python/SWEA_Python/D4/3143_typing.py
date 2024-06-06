# 가장 빠른 문자열 타이핑

def proc_patt(patt):
    patt_list = [0] * 128
    patt_len = len(patt)
    for i in range(patt_len - 1):
        patt_list[ord(patt[i])] = i + 1
    return patt_list


def boyer_moore(patt, text):

    jump_list = proc_patt(patt)
    patt_len = len(patt)
    i = patt_len
    j = 1
    count = 0
    while i - j < len(text):
        jump_size = patt_len - jump_list[ord(text[i-j])]
        if j > patt_len:
            count += 1
            # i += jump_size
            i += patt_len
            j = 1
            continue
        if text[i-j] != patt[patt_len - j]:
            i += jump_size
            j = 1
            continue
        j += 1

    return count
     

T = int(input())
for t in range(T):
    str2, str1 = input().split()
    patt_count = boyer_moore(str1, str2)
    ans_count = len(str2) - (len(str1) - 1) * patt_count
    print(f'#{t+1} {ans_count}')