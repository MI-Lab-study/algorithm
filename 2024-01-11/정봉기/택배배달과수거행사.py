def solution(cap, n, deliveries, pickups):
    answer, dcap, pcap = 0, 0, 0

    for i in range(n - 1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            tmp = 0
            while dcap < deliveries[i] or pcap < pickups[i]:
                tmp += 1
                dcap += cap
                pcap += cap
            dcap -= deliveries[i]
            pcap -= pickups[i]
            answer += ((i + 1) * tmp * 2)
    return answer

