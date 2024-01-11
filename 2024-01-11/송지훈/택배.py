def solution(cap, n, deliveries, pickups):
    import math
    answer, dcap, pcap = 0, 0, 0

    for i in range(n-1, -1, -1):
        if deliveries[i]!=0 or pickups[i]!=0:
            tmp = max(math.ceil((deliveries[i]-dcap)/cap), math.ceil((pickups[i]-pcap)/cap))
            dcap += tmp*cap
            pcap += tmp*cap
            
            dcap -= deliveries[i]
            pcap -= pickups[i]
            answer += ((i + 1) * tmp * 2)

    return answer