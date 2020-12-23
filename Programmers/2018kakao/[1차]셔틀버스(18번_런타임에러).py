from collections import deque
import datetime

def ans_time(a,b,time):
    b=b+time
    if b>=60:
        a+=(b//60)
        b%=60
    elif b<0:
        b+=60
        a-=1
    ans=str(datetime.time(a,b,0))
    ans=ans.split(":")[0]+":"+ans.split(":")[1]
    return ans
        
def bus(n,t):
    bus_list=["09:00"]
    if n<=1:
        return bus_list
    else:
        for i in range(1,n):
            h,m=bus_list[i-1].split(":")
            time=ans_time(int(h),int(m),t)
            bus_list.append(time)
    return bus_list

def solution(n, t, m, timetable):
    timetable.sort()
    q=deque(timetable)
    bus_time=bus(n,t)

    for i in range(len(q)-1,-1,-1):
        if q[i]>bus_time[n-1]:
            q.pop()

    #######################################################
    if n<=1 and len(q)<m: #버스가 한대 수용인원이 여유있는경우
        return "09:00"
    #######################################################
    elif n<=1 and len(q)>=m: #버스가 한대 수용인원이 넘칠경우
        for i in range(m):
            crew=q.popleft()
            if str(crew)>"09:00":
                return "09:00"
            if i==m-1:
                a,b=crew.split(":")
                time=ans_time(int(a),int(b),-1)
                return time
    #######################################################
    elif n>1 and len(q)<m: #버스가 여러대 수용인원이 여유있는경우
        return bus_time[n-1]
    #######################################################
    elif n>1 and len(q)>=m: #버스가 여러대 수용인원이 넘칠경우
        for i in range(len(bus_time)-1): #버스 시간 --> 마지막 버스까지만 진행
           for j in range(m): #태울 인원 확인
               if q[j]<=bus_time[i]:
                   q.popleft() #탑승

        ########### 여기서 다시 버스한대
        if len(q)>=m:#기다리는 사람이 있는경우
            a,b=q[m-1].split(":")
            return ans_time(int(a),int(b),-1)
        else:
            return bus_time[n-1]
    #######################################################