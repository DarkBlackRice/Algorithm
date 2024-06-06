# 병합 정렬 1


# 함수 선언
def save_count(lst, data):
    # K 만큼 카운팅 되었을 때, 저장되는 수를 뱉고 프로그램 종료
    global count
    count += 1
    # print(count) # 디버깅 프린트
    if count == K:
        print(data)
        exit(0)
    
    else: # ~ 여기까지 : 이 부분을 지우면 그냥 병합정렬
        lst.append(data)


def merge(lst1, lst2):
    # print('들어온 값 : ',lst1, lst2) # 디버깅 프린트
    
    i, j = 0, 0
    temp_list = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            temp = lst1[i]
            i += 1
        else:
            temp = lst2[j]
            j += 1
        
        # K 만큼 카운팅 되었을 때, 저장되는 수를 뱉고 프로그램 종료
        save_count(temp_list,temp)
    
    if i == len(lst1):
        for k in lst2[j:]:
            save_count(temp_list,k)
    else:
        for k in lst1[i:]:
            save_count(temp_list,k)
    
    # print('나온 값 : ',temp_list) # 디버깅 프린트
    return temp_list


def merge_sort(lst):
    num = len(lst)
    if num >= 2:
        # print(lst[:(num+1)//2], lst[(num+1)//2:]) # 디버깅 프린트
        return merge(merge_sort(lst[:(num+1)//2]), merge_sort(lst[(num+1)//2:]))
    else:
        return lst


# 본 코드
count = 0

N, K = map(int,input().split())

merge_sort(list(map(int,input().split())))
print(-1)

