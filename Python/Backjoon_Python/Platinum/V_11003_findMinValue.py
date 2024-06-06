# 최솟값 찾기
import sys; input = sys.stdin.readline

# 전략 : 덱을 사용해서 최솟값을 관리하자.
from collections import deque

N, L = map(int, input().split())
data = list(map(int, input().split()))

# 데이터는 인덱스와 값을 튜플로 관리(enumerate형식)
arr = deque([(0,data[0])])
print(arr[0][1], end=' ')

for i in range(1, N):
    # 1. arr 안에서의 1번 인덱스값은 오름차순으로 유지된다.
    #   : 오름차순이란 0번 값이 빠지면 1번 값이 최솟값이라는 뜻이다.
    #   (뒤에 들어온 값보다 크면 다 제거됨
    #       - L구간이 유지되는 와중에 더 큰 값이 존재하는게 의미 X)
    while arr and arr[-1][1] > data[i]:
        arr.pop()
    arr.append((i, data[i]))

    # 2. i에서 L 이상 떨어진 값들을 제거
    # 만약 2번을 먼저 하면, L == 1인 경우에 문제가 생길 수 있다.
    # (하나 있을 때 하나만 빠져도 멈출 수 있는 트리거가 없다)
    while arr[0][0] <= i-L:
        arr.popleft()
    print(arr[0][1], end=' ')
