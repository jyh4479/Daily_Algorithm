N,M=map(int,input().split())
cur_y,cur_x,cur_dir=map(int,input().split())
arr=[[int(line) for line in input().split()] for i in range(N)]#이 부분 복습

dir_y=[0,1,0,-1]
dir_x=[-1,0,1,0]

arr[cur_y][cur_x]=-1 #현위치 방문 체크
cnt=1 #현위치 방문

def check_path():
    for i in range(4): #4방향 중 갈 수 있는 곳이 있는지 체크
        if(arr[cur_y+dir_y[i]][cur_x+dir_x[i]]==0): #방문 가능한 곳이 존재
            return False
    return True #방문 가능한 곳이 없음
def left(cur_dir):
    if(cur_dir==0):
        return 3
    else:
        cur_dir-=1
        return cur_dir
def move_back(cur_dir, cur_y, cur_x):
    if(cur_dir==0): #북
        cur_y+=1
        if(arr[cur_y][cur_x]==1):
            return True, cur_y, cur_x
        else:
            return False, cur_y, cur_x
    elif(cur_dir==1): #동
        cur_x-=1
        if(arr[cur_y][cur_x]==1):
            return True, cur_y, cur_x
        else:
            return False, cur_y, cur_x
    elif(cur_dir==2): #남
        cur_y-=1
        if(arr[cur_y][cur_x]==1):
            return True, cur_y, cur_x
        else:
            return False, cur_y, cur_x
    elif(cur_dir==3): #서
        cur_x+=1
        if(arr[cur_y][cur_x]==1):
            return True, cur_y, cur_x
        else:
            return False, cur_y, cur_x

while(1):
    if(check_path()):
        flag,cur_y,cur_x=move_back(cur_dir, cur_y, cur_x)
        if(flag):
            print(cnt)
            break

    if(arr[cur_y+dir_y[cur_dir]][cur_x+dir_x[cur_dir]]==1 or arr[cur_y+dir_y[cur_dir]][cur_x+dir_x[cur_dir]]==-1): #왼쪽이 바다 또는 이미 방문인 경우 회전
        cur_dir=left(cur_dir)
    else: #왼쪽이 갈 수 있는 경우
        cur_y+=dir_y[cur_dir] #전진
        cur_x+=dir_x[cur_dir]
        cnt+=1
        arr[cur_y][cur_x]=-1 #방문 체크
        cur_dir=left(cur_dir)
