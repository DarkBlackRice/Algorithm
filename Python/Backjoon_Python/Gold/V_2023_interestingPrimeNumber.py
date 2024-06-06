# 신기한 소수


def is_prime(num):
    until = int(num**(1/2)) + 1
    for i in range(2, until):
        if not num%i:
            return False
    return True


def dfs(string, k):
    if k == N:
        if is_prime(int(string)):
            print(string)
            return
    for i in range(1,10,2):
        n_string = string + str(i)
        if is_prime(int(n_string)):
            dfs(n_string, k+1)


N = int(input())
dfs('2', 1)
dfs('3', 1)
dfs('5', 1)
dfs('7', 1)
