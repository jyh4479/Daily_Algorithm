def change_mili(num):
    if len(num)==1:
        return int(num)*100
    elif len(num)==2:
        return int(num)*10
    else:
        return int(num)

def time_change(lines):
    time_list,delay_list=[],[]
    for line in lines: #시간, 딜레이 분리
        time_list.append(line.split()[1])
        delay_list.append(line.split()[2])

    mili_list=[]
    for time in time_list: #시간 변환
        hour=int(time.split(":")[0])*60*60*1000
        min=int(time.split(":")[1])*60*1000
        sec=int(time.split(":")[2].split(".")[0])*1000
        mili=int(time.split(":")[2].split(".")[1])
        sum=hour+min+sec+mili
        mili_list.append(sum)

    mili_delay_list=[] #딜레이 변환 --> 여기 다시해야함
    for time in delay_list:
        time=str(time).replace("s","")
        if "." in time:
            sec=int(time.split(".")[0])*1000
            mili=change_mili(time.split(".")[1])
        else:
            sec=int(time.split(".")[0])*1000
            mili=0
        sum=sec+mili
        mili_delay_list.append(sum)

    return mili_list,mili_delay_list

def ans(time, delay):
    num=0
    end_time=time
    start_time=[]
    for i in zip(time,delay):
        start_time.append(i[0]-i[1]+2)
        #print(start_time)

    for i in range(len(start_time)):
        base_start_time=start_time[i]
        number=0
        for j in zip(start_time,end_time):
            if j[1]<base_start_time or j[0]>base_start_time+1000:
                continue
            else:
                number+=1
        num=max(number,num)

    for i in range(len(start_time)):
        base_start_time=end_time[i]
        number=0
        for j in zip(start_time,end_time):
            if j[1]<base_start_time or j[0]>base_start_time+1000:
                continue
            else:
                number+=1
        num=max(number,num)
    return num

def solution(lines):
    time,delay=time_change(lines) #밀리초로 변환
    return ans(time,delay)