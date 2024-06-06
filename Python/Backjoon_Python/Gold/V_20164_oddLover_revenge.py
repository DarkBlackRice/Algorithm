# 홀수 홀릭 호석

# 홀수 카운팅 함수
def count_odd(string):
    cnt = 0
    for n in string:
        if int(n) % 2:
            cnt += 1
    return cnt


# 탐색 함수
def dfs(string, cnt):
    if len(string) == 1:
        global ans
        ans.append(cnt + count_odd(string))
        return
    
    elif len(string) == 2:
        n_str = str(int(string[0]) + int(string[1]))
        dfs(n_str, cnt + count_odd(string))

    elif len(string) >= 3:
        cases = []
        length = len(string)
        temp_cnt = count_odd(string)
        for i in range(1, length-1):
            for j in range(i+1, length):
                cases.append(str(int(string[:i]) + int(string[i:j]) + int(string[j:])))
        for case in cases:
            dfs(case, cnt + temp_cnt)


# 본 코드
N = input()
ans = []
dfs(N, 0)
print(min(ans), max(ans))
