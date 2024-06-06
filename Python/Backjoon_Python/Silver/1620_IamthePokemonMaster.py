# 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())
test = {}

# 도감 채우기
name_data = ['',]
num_data = {}
for i in range(1, N+1):
    data = input()
    name_data.append(data)
    num_data[data] = i

# 문제의 답 출력하기
for _ in range(M):
    input_data = input()
    if input_data.isdigit():
        print(name_data[int(input_data)])
    else:
        print(num_data.get(input_data))
