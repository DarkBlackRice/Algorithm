# 단어 뒤집기 2

S = input()
n = 0
parsed_str_dict = {}
order = 0
new_str = ''

while n < len(S): # 받은 str 파싱하기

    if S[n] == '<':    # <태그> 선별하기
        start_tag_index = n
        while True:    # 태그 시퀀스 작동
            n += 1
            if S[n] == '>':
                end_tag_index = n
                break
        parsed_str_dict[(order,S[start_tag_index:end_tag_index+1])] = 'tag'                
    elif S[n] != ' ':    # 문자 공백 기준으로 자르기 --> 공백 아니면 (공백 전) or ('<' 전) or (끝나기 전) 까지 서칭
        start_word_index = n
        while True:
            if n < len(S)-1: # 문자열의 끝이 아닐 때,
                if (S[n+1] == ' ') or (S[n+1] == '<'):
                    end_word_index = n
                    break
            else: # 문자열의 끝일 때,
                end_word_index = n
                break
            n += 1
        parsed_str_dict[(order,S[start_word_index:end_word_index+1])] = 'word'
    else: # 공백도 처리해줘야 하지요
        parsed_str_dict[(order,S[n:n+1])] = 'void'

    order += 1
    n += 1

# 문자 뒤집기
parsed_str_list = sorted(list(parsed_str_dict.keys())) 
for dict_data in parsed_str_list:
    if parsed_str_dict[dict_data] == 'word':
        rev_str = dict_data[1][::-1]
        new_str += rev_str
    else:
        new_str += dict_data[1]

print(new_str)