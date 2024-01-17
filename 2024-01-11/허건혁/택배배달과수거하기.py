def update(A, idx, cap):
    pivot = 0
    while cap >= pivot and idx >= 0:
        pivot += A[idx]
        A[idx] = 0
        idx -= 1
    A[idx + 1] += pivot - cap
    return A, idx + 1


def solution(cap, n, deliveries, pickups):
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    while not (deliveries[n] + pickups[n]) and n:
        n -= 1

    p_idx = d_idx = n
    result = 0
    while d_idx + p_idx:
        result += max(p_idx, d_idx)
        deliveries, d_idx = update(deliveries, d_idx, cap)
        pickups, p_idx = update(pickups, p_idx, cap)
    return result * 2
