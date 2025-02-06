from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    time = 0
    currentWeight = 0
    # 트럭이 남아 있으면 돌아야함
    # 현 다리의 무게가 0보다 크면 돌아야함
    while len(truck_weights) > 0:
        time += 1
    
        currentWeight = currentWeight - bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
    return time + bridge_length