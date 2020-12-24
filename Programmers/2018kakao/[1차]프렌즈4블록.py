def run_delete(m,n,board,visit):
    ans=0
    for i in range(m): #블록 없애기
        for j in range(n):
            if visit[i][j]==True:
                ans+=1
                board[i][j]="/"
                visit[i][j]=False

    for i in range(m-2,-1,-1):#블록 내리기
        for j in range(n):
            if board[i][j]!="/" and board[i+1][j]=="/": #내릴수있는경우
                next,prev=i+1,i
                while next<m and board[next][j]=="/":
                    board[prev][j],board[next][j]=board[next][j],board[prev][j] #내리기
                    prev,next=next,next+1
    return ans

def check_delete(m,visit):
    for i in range(m):
        if True in visit[i]:return False
    return True

def delete_block(i,j,board,visit):
    text=board[i][j]
    if board[i][j+1]!=text:return #4개가 완성이 안되는경우
    if board[i+1][j]!=text:return
    if board[i+1][j+1]!=text:return

    ################## 삭제할 블록 체크
    visit[i][j]=True
    visit[i][j+1]=True
    visit[i+1][j]=True
    visit[i+1][j+1]=True
    ##################
    return

def solution(m, n, board):
    map=[list(board[i]) for i in range(m)] #문자열들 리스트화
    board=map

    visit=[[False for _ in range(n)]for _ in range(m)]

    ans=0
    while True:
        for i in range(m-1): #없앨 블록 찾기
            for j in range(n-1):
                if board[i][j]!="/":
                    delete_block(i,j,board,visit)
        if check_delete(m,visit):break #제거할게 없을때까지 반복
        ans+=run_delete(m,n,board,visit)

    return ans