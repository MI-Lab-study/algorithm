def solution(cap, n, deliveries, pickups):
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            start = i
            end = i+1
            break
        else:
            start, end = -1, 0
    
    total_path = 0

    while start >= 0:
        if sum(deliveries[start:end]) > cap or sum(pickups[start:end]) > cap:
            total_path += 2*end

            subs = cap
            for i in range(end-1, -1, -1):     # 맨 끝부터 subs가 0이 될때까지
                if deliveries[i]-subs >= 0:
                    deliveries[i] -= subs
                    break
                else:
                    subs -= deliveries[i]
                    deliveries[i] = 0

            subs = cap
            for i in range(end-1, -1, -1):     # 맨 끝부터 subs가 0이 될때까지
                if pickups[i]-subs >= 0:
                    pickups[i] -= subs
                    break
                else:
                    subs -= pickups[i]
                    pickups[i] = 0

            end = start+1
            start = end-1

        elif start == 0:
            if sum(deliveries[start:end]) == 0 and sum(pickups[start:end]) == 0:     
                total_path += 0
            else:
                total_path += 2*end
            start -= 1
        else:
            start -= 1
            
    return total_path