duck_sounds = input()
ref_sound = 'quack'
num_of_duck = 0
now_processing = []
max_duck = 0


for sound in duck_sounds:
    id = 0

    if sound == ref_sound[0]: # 식별된 소리가 q일 때
        num_of_duck += 1
        now_processing.append(0) # 
        id = 1
    elif sound in ref_sound[1:]:
        for i in range(len(now_processing)):
            if ref_sound[now_processing[i]+1]==sound:
                now_processing[i] += 1
                id = 1
                break     

    if id == 0:
        max_duck = -1
        break 

    if max_duck < num_of_duck:
        max_duck = num_of_duck

    if 4 in now_processing:
        now_processing.remove(4)
        num_of_duck -= 1

if now_processing != []:
    print(-1)
else:
    print(max_duck)   


