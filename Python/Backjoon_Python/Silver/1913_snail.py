#달팽이

N = int(input())
num = int(input())
snailList = []

for i in range(N):
    snailList.append([0]*N)

startPoint=(N//2,N//2)
y,x=startPoint
getCoord = [y,x]

snailList[y][x]=1
nowNum = 2

for i in range(1,N):
    if i%2==1:
        for j in range(1,i+1):
            y-=1
            snailList[y][x]=nowNum
            if nowNum==num:
                getCoord=(y,x)
            nowNum+=1
        for j in range(1,i+1):
            x+=1
            snailList[y][x]=nowNum
            if nowNum==num:
                getCoord=(y,x)
            nowNum+=1
    elif i%2==0:
        for j in range(1,i+1):
            y+=1
            snailList[y][x]=nowNum
            if nowNum==num:
                getCoord=(y,x)
            nowNum+=1
        for j in range(1,i+1):
            x-=1
            snailList[y][x]=nowNum
            if nowNum==num:
                getCoord=(y,x)
            nowNum+=1

for i in range(N-1):
    snailList[N-2-i][0] = nowNum
    if nowNum==num:
        getCoord=(N-2-i,0)
    nowNum+=1

for i in range(N):
    for j in range(N):
        print(snailList[i][j],end=" ")
    print()

y,x = getCoord
print('%d %d'%(y+1,x+1))



    
 