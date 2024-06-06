# 패턴 마디의 길이

T = int(input())

for t in range(1,T+1):
    user_input = input()
    for i in range(1,31,2):
        mid_index = i//2+1
        first_part = user_input[:mid_index]
        last_part = user_input[mid_index:i+1]
        if first_part==last_part:
            print(f"#{t} {len(user_input[:i//2+1])}")
            break
