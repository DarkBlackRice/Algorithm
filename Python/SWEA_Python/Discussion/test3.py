# 

# 순열함수
def idx_dfs(lst, depth):
    global idx_sequence

    if depth==n:
        idx_sequence.append(lst)
        print(lst, end=' ') # 디버깅 프린트
        return

    for i in range(n):
        if visit_idx[i]==0:
            # lst.append(i) # 이래말고
            visit_idx[i]=1
            idx_dfs(lst+[i], depth+1) # 요래 하는건 어떰
            visit_idx[i]=0


# 저울 다는 경우의 수 구하는 함수 : 결과물 2진수로 나옴
def dfs(idx, depth):
    global ans,n,count
    if depth==n:
        print(bit, end = ' ')

        if bit == [0]*n: # 다 오른쪽에 두는 경우는 카운팅 안 함
            return

        if bit == [1]*n: # 다 왼쪽에 두는 경우는 n!개 전부 정답
            ans+=factorial[n]
            return

        for i in range(len(idx_sequence)):
            count += 1
            if bit[idx_sequence[i][0]]==0: # 첫 번째 추를 오른쪽에 두면 카운팅 안함
                # print(bit, idx_sequence[i]) # 디버깅 프린트
                # return # 찾았다 문제아
                continue

            l = r = 0
            for idx in idx_sequence[i]:
                if bit[idx]==1:
                    l+=arr[idx]
                else:
                    r+=arr[idx]
                if l<r:
                    # print(bit, idx_sequence[i]) # 디버깅 프린트
                    break

            # l>=r
            else:
                # print(bit, idx_sequence[i]) # 디버깅 프린트
                ans+=1
        return

    for i in range(2):
        bit[idx]=i
        dfs(idx+1,depth+1)


# 팩토리얼 DP파트
factorial = [0]*(10)
factorial[0] = factorial[1] = 1
for i in range(2,10):
    factorial[i] = factorial[i-1]*i

# 본 함수부
for t in range(1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    bit=[0]*n

    visit_idx = [0]*n
    idx_sequence = []

    #디버깅용
    count = 0

    print('0~N 까지의 순열') # 디버깅 프린트
    idx_dfs([],0)
    print('\n---------------') # 디버깅 프린트

    print('무게 추의 위치 경우의 수') # 디버깅 프린트
    dfs(0,0)
    print('\n---------------') # 디버깅 프린트
    print(f'#{t+1} {ans}')