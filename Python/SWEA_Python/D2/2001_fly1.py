# 파리 퇴치

def cnt_fly(row,col): # 좌표를 매개변수로 받았죠
    cnt = 0 # 파리를 세어야하니까 초기화 해줍시다.
    
    for r in range(row,M+row):      # 시작 지점은 받은 좌표부터
        for c in range(col,M+col):  # 종료지점은 그것보다 M만큼 더 간 곳까지
            cnt += board[r][c]      # input 받은 보드에서 찾아 더해줍니다
    return cnt # 센 파리수를 반환

T = int(input())

for t in range(T):

    N, M = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(N)]
    # 여러 줄 인풋받는 방법 : list comprehension 쓴 겁니다! 우리 배웠었죠!

    max_fly = 0 # 매 가장 좌측상단 좌표를 기준으로 파리를 세어줄 겁니다.
                # for 문 돌기 전에 초기화 해줍시다.

    for i in range(1+N-M): # 여기서 range() 함수 안의 값이 이렇게 설정된 이유는
        for j in range(1+N-M): # 그림으로 추가 절명 드리겠습니다.

            temp = cnt_fly(i,j) # 각 좌표마다 M x M 범위의 파리 마리수를
                                # 함수를 통해 구해줍니다.
            
                                # 사실 이 위치에 상단의 함수 코드를 넣으면
                                # 잘 돌아가긴 합니다만,
                                # 이후 탐색 문제는 함수로 푸는게
                                # 편할 때가 있어요.

            if max_fly < temp: # 이제 각 좌표에서 받아온 파리수를 비교해서
                max_fly = temp # 가장 큰 값을 골라줍니다.

    print(f'#{t+1} {max_fly}') # 케이스 번호에 맞추어 출력해주면 끝!