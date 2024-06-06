# 기차가 어둠을 헤치고 은하수를
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trains = [[0]*20 for _ in range(N)]
cmds = [list(map(int,input().split())) for _ in range(M)]
cnt = 0

for cmd in cmds:
    if cmd[0] == 1:
        trains[cmd[1]-1][cmd[2]-1] = 1
    elif cmd[0] == 2:
        trains[cmd[1]-1][cmd[2]-1] = 0
    elif cmd[0] == 3:
        trains[cmd[1]-1].pop()
        trains[cmd[1]-1].insert(0,0)
    elif cmd[0] == 4:
        del trains[cmd[1]-1][0]
        trains[cmd[1]-1].append(0)

# for i in range(N):
#     print(*trains[i])

psd_train = []
for train in trains:
    if train not in psd_train :
        cnt += 1
        psd_train.append(train)

print(cnt)

# 삐트연싼으로만뜰어뽀끼씨빨쒸프트키까안빠쪄요
