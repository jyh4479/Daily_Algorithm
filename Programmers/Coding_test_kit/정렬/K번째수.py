def solution(array, commands):
    ans=[]
    for cmd in commands:
        i,j,k=cmd[0]-1,cmd[1],cmd[2]-1
        if i==j:
            ans.append(array[i])
        else:
            ans.append(sorted(array[i:j])[k])
    return ans