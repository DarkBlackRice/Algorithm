# 후위 표기식

# 수정사항 0. 연산자가 늘어났으므로 수정
isp = {'(':0, '+':1, '-':1, '/':2, '*':2}
icp = {'(':3, '+':1, '-':1, '/':2, '*':2}
 
def postfix(data):
    stack = []
    result = []
    for d in data:
        # 수정사항 1. 숫자가 아니라 알파벳이 들어오니 메서드 교체
        # .isdigit() --> .isalpha()
        if d.isalpha():
            result.append(d)
        else:
            if d == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                if not stack:
                    return 'error'
                stack.pop()
            else:
                while stack and isp[stack[-1]] >= icp[d]:
                    result.append(stack.pop())
                stack.append(d)
 
    return result

# 처음 시작과 끝에 괄호로 감싸져있어야 위의 함수가 잘 돌아감
# --> 따라서 데이터를 괄호로 감싸서 postfix 함수에 넣기
data = '(' + input() + ')'
print(''.join(postfix(data)))
