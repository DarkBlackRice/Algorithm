# 파일 정리

N = int(input())
ext_dict = {}

files = [input() for _ in range(N)]

for file in files:
    ext = file.split('.')[1]
    if ext not in ext_dict:
        ext_dict[ext] = 1
    else:
        ext_dict[ext] += 1

for ext in sorted(list(ext_dict.keys())):
    print(ext, ext_dict[ext])