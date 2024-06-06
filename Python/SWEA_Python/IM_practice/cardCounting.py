# 영준이의 카드 카운팅

ref = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

def card_count(data):
    global ans
    for r in range(4):
        cnt = 0
        for c in range(1, 14):
            if data[r][c] > 1:
                ans = ['ERROR']
                return
            elif not data[r][c]:
                cnt += 1
        ans.append(cnt)
    return


T = int(input())
for t in range(T):
    card_data = input()
    N = len(card_data)
    deck = [[0]*14 for _ in range(4)]
    for i in range(0, N, 3):
        card_num = 0
        for j in [1,2]:
            card_num = card_num*10 + int(card_data[i+j])
        deck[ref[card_data[i]]][card_num] += 1

    ans = []
    card_count(deck)
    print(f'#{t+1}', *ans)