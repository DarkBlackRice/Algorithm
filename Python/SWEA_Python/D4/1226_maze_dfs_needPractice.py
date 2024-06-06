def findStart(map): #미로 시작점 찾기 함수
    startPoint=[-1,-1] #얼탱이 없는 값으로 선언
    for i in range(16): 
        if 2 in map[i]: 
            startPoint[0] = i
            startPoint[1] = map[i].index(2) #미로에서 2를 찾고 2의 좌표위치 startPoint변수에 저장
            return tuple(startPoint) #tuple로 해야 변수 복수개에 저장하기 좋다
  
def dfs(map,coord):#coord는 좌표 : tuple형식으로 줄 것!
    result = 0 #결과 플래그변수
    visited=[] #방문한 좌표
    noLonger=[] #더이상 방문할 필요가 없는 좌표
    visited.append(coord) #visited 리스트에 가장 마지막 값이 현위치
    dx=[0,0,1,-1]
    dy=[1,-1,0,0] #아아.. 이것은 델타함수(탐색순서지정)라는 것이다..

    while visited: #visited = [] 일때는 안 가본 곳은 벽말고 없다는 뜻 -> 그러면 함수 종료
        findNew = 0
        x,y=visited[-1] #현위치 받기 -> while 루프가 한 번 돌았다면, 갱신된 현위치 호출
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] #델타함수를 써서 상,하,우,좌 순으로 탐색
            if nx in range(16) and ny in range(16): #새위치 후보가 일단 미로 안에 있는지 확인
                if (map[nx][ny]!= 1) and ((nx,ny) not in visited) and ((nx,ny) not in noLonger): #벽(1)과 막다른 길이 아닌 길을 찾았다면
                    visited.append((nx,ny)) #현위치 갱신
                    if map[nx][ny]==3: #현위치가 혹시 도착지인지..?
                        result = 1 #찾았다!
                        return result
                    else: #아니넹...
                        findNew = 1 #그래도 새 길은 찾았군
                        break #도착지가 아니면 갱신주소 들고 처음으로 복귀(17: while visited ~)
        if findNew == 0: #새 위치를 찾지 못하고 델타함수반복을 빠져나오면
            noLonger.append(visited.pop()) #그 좌표는 pop해서 noLonger리스트(막다른 길)에 넣자.
    return result

ans=[]

for i in range(10):
    testTime=int(input())
    mazeMap=[list(map(int,input())) for _ in range(16)]
    ans.append(dfs(mazeMap,findStart(mazeMap)))

for i in range(10):
    print('#%d %d'%(i+1,ans[i]))
