# 최대 상금

def swap(fst, snd, num):
    # 변경할 위치를 fst 와 snd 로 받았다.
    # num 을 문자열로 받았다는 사실을 잊지말자.
    lst = list(num)                             # 문자열을 리스트로 바꿔준 후에
    lst[fst], lst[snd] = lst[snd], lst[fst]     # 변경위치를 참조하여 바꿔주자.
    return ''.join(lst)     # 리스트를 문자로 바꿔서 return 해줍시다.


def reward(k, num):
    global ans
    # 메모이제이션 파트
    for i in range(720):        # 최대 가로길이 720인 리스트를 돌면서
        if memo[k][i] == num:   # 만약 memo 리스트에 저장된 수가 현재 수와 같다면
            return              # 처리할 예정이므로 굳이 볼 필요 없음 --> return : 가지치기

        elif not memo[k][i]:    # 저장된 값 다 돌았는데 중복이 없었다? --> 새 숫자
            memo[k][i] = num    # 새 숫자니까 잘 저장해줍시다.
            break               # 더 이상 돌 필요 X --> for i in range(720) 탈출

    if k == K:
        ans = max(ans, int(num))    # num 은 숫자열이다. int()함수를 걸어주자.
        return

    # 조합을 for 문으로 구현했다.
    for i in range(N-1):
        for j in range(i+1, N):
            # 단계를 1 올려주고, 자리를 바꾼 수 함수로 받아와 매개변수로 넘겨주자.
            reward(k+1, swap(i, j, num))


T = int(input())
for t in range(T):

    # number와 K는 각각 숫자판과 교환횟수로
    # 둘 다 문자열로 그대로 받아온다.
    number, K = input().split()

    # K는 정수로 바꿔주고, 숫자판의 길이를 N으로 설정
    K = int(K)
    N = len(number)

    # 메모이제이션을 하기위한 저장보드
    memo = [[0]*720 for _ in range(K+1)]

    # 최댓값을 ans 에 저장한다.
    ans = 0

    # reward 함수에 단계 0과 숫자판 number 를 "문자열"로 넣어준다.
    reward(0, number)
    print(f'#{t+1} {ans}')

