def solution(routes):
    ans = 1 #default ans
    array = sorted(routes, key = lambda x : x[0])

    cameraPoint = array[0][1] #check point
    for i in range(1, len(array)):
        startPoint, endPoint = array[i][0], array[i][1]
        if startPoint > cameraPoint:
            ans += 1
            cameraPoint = endPoint
            continue
        if endPoint < cameraPoint:
            cameraPoint = endPoint

    return ans