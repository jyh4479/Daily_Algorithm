from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights=deque(truck_weights)
    bridge=deque([0 for _ in range(bridge_length)])
    answer=0
    weightSum=0
    while truck_weights or weightSum!=0:
        if truck_weights:
            truck=truck_weights.popleft()
            weightSum-=bridge.popleft()
            
            if weightSum+truck>weight: #못올라가는경우
                bridge.append(0)
                truck_weights.appendleft(truck)
            else:
                bridge.append(truck)
                weightSum+=truck
        
        else:
            weightSum-=bridge.popleft()
            bridge.append(0)
        answer+=1
        
    return answer
