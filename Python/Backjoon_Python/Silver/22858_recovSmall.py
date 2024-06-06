# 원상 복구 (small)

import sys
input = sys.stdin.readline() # 안 해도 풀리지만 하면 시간단축 5배 !!!

N, K = map(int,input().split())

result_list =list(map(int,input().split()))
D_list = list(map(int,input().split()))
origin_list = list(range(N)) # 정렬된 origin_list를 주어진 규칙대로 섞어서 결과값과 비교

for k in range(K):
    shuf_list = [] # 여기에 섞은 결과값을 임시저장
    for d in D_list:
        shuf_list.append(origin_list[d-1])
    origin_list = shuf_list # 원래 카드리스트에 섞인 결과값 저장

results = sorted(zip(origin_list,result_list))
#sort하면 제일 앞 원소 기준으로 정렬! --> 이렇게 하면 섞기 전 카드 순서가 두번째 원소로 나옴! 

for result in results: # 순서대로 출력~
    print(result[1], end =' ')
