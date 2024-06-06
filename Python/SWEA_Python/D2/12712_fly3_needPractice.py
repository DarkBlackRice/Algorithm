# 파리 퇴치 3

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    wall = [list(map(int,input().split())) for n in range(N)]
    plus_dx = [1,-1,0,0]
    plus_dy = [0,0,1,-1]
    cross_dx = [1,1,-1,-1]
    cross_dy = [1,-1,1,-1]  #델타 함수는 유용하나, 언제 사용할 수 있는지 확인할 필요가 있다.
    max_count = 0

    for x in range(N):
        for y in range(N):
            plus_count = wall[x][y]
            cross_count = wall[x][y]

            for m in range(1, M):
                for i in range(4):
                    px = x + plus_dx[i]*m
                    py = y + plus_dy[i]*m
                    cx = x + cross_dx[i]*m
                    cy = y + cross_dy[i]*m

                    if 0<=px<N and 0<=py<N :
                        plus_count += wall[px][py]

                    if 0<=cx<N and 0<=cy<N :
                        cross_count += wall[cx][cy]

            if max_count<plus_count:
                max_count = plus_count
            if max_count<cross_count:
                max_count = cross_count

    print(f"#{t} {max_count}")
