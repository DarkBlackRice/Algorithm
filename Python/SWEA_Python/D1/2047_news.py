# 신문 헤드라인

string = input()
printString = []

for w in string:
    if ord(w) in range(97,123):
        printString.append(chr(ord(w)-32))
    else:
        printString.append(w)

result = ''.join(printString)

print(result)






