# 홀수 홀릭 호석
import sys
input = sys.stdin.readline

# 재귀를 사용하여 다시 풀어보자.

split_map = {}

def split_num(string,input_map):

    temp_list = []

    if len(string) >= 3:
            for i in range(1,len(string)-1):
                for j in range(i+1, len(string)):
                    temp_list.append(str(int(string[:i]) + int(string[i:j]) + int(string[j:])))

    elif len(string) == 2:
            temp_list.append(str(int(string[0]) + int(string[1])))

    input_map[string] = temp_list

    return 


def count_odd(string):
    
    count = 0
    is_num_single = False
    retrun_num = string
    now = string

        



    return 
    


N = input()

min_value = -1
max_value = -1

split_num(N,spilt_map)


        

