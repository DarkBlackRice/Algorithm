# 단어 공부

string = input().upper()
cnt = [0] * 26
for c in string:
    cnt[ord(c) - ord('A')] += 1

ans = 0
flag = False
for i in range(26):
    if cnt[i] >= cnt[ans]:
        # 여기서 실수가 남 : ans가 아니라 i가 0이 아닐때, 즉 가장 초기 시도가 아닐때에 해당해야한다.
        if i != 0 and cnt[i] == cnt[ans]:
            flag = True
        else:
            flag = False
            ans = i

if flag:
    print('?')
else:
    print(chr(ans + ord('A')))
