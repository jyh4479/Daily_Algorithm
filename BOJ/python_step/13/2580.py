import sys #pypy3에서 동작
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(9)]
stack=[]

for i in range(9): #0 위치 저장
    for j in range(9):
        if graph[i][j]==0:
            stack.append([i,j])

def print_graph():
    for i in range(9):
        for j in graph[i]:
            print(j,end=" ")
        print()

def check(num_list,i,j):
    a=i//3
    b=j//3
    for y in range(a*3,a*3+3): #3*3검색
        for x in range(b*3,b*3+3):
            if graph[y][x] in num_list:
                num_list.remove(graph[y][x])
    for y in range(9): #세로
        if graph[y][j] in num_list:
            num_list.remove(graph[y][j])
    
    for x in range(9): #가로
        if graph[i][x] in num_list:
            num_list.remove(graph[i][x])
    return num_list

def dfs(cnt):
    if cnt==len(stack):
        print_graph()
        exit()
        return
    else:
        num_list=[i for i in range(1,10)]
        ny=stack[cnt][0]
        nx=stack[cnt][1]
        available_list=check(num_list,ny,nx)
        for i in available_list:
            graph[ny][nx]=i
            dfs(cnt+1)
            graph[ny][nx]=0
dfs(0)

"""시간초과 (해당 코드는 백트래킹이라기보단 DFS로 비효율적 완전탐색을 해버림 답은 맞음)
#maps=[list(map(int,input().split())) for _ in range(9)]-->초기화법

maps=list() #map은 예약어라서 append시 오류가 났던것
location=list()

def check(location):
    for i in range(len(location)):
        y,x=location[i][0],location[i][1]

        num_list=[False for _ in range(9)] #행 검사
        for a in range(9): 
            if num_list[maps[a][x]-1]==True:
                return False
            elif num_list[maps[a][x]-1]==False:
                num_list[maps[a][x]-1]=True

        num_list=[False for _ in range(9)] #열 검사
        for a in range(9):
            if num_list[maps[y][a]-1]==True:
                return False
            elif num_list[maps[y][a]-1]==False:
                num_list[maps[y][a]-1]=True

        num_list=[False for _ in range(9)] #3*3 검사
        for a in range(9):
            for b in range(9):
                if num_list[maps[a][b]-1]==True:
                    return False
                elif num_list[maps[a][b]-1]==False:
                    num_list[maps[a][b]-1]==True
    return True

def dfs(cnt):
    if cnt==len(location) and check(location): #모든 수를 채운 경우
        print(maps)
        exit(0)
        return
    elif(cnt==len(location)): #숫자가 다 채워진 경우
        return
    else:
        for a in range(1,10): #해당 좌표에 놓을 수
            ny,nx=location[cnt][0],location[cnt][1]
            maps[ny][nx]=a
            dfs(cnt+1)
            maps[ny][nx]=0

for _ in range(9):
    maps.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if maps[i][j]==0:
            location.append([i,j])

dfs(0)
"""
