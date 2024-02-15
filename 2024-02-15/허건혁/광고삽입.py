def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    def time2int(s):
        return int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:])

    def int2time(s):
        h, s = divmod(s, 3600)
        m, s = divmod(s, 60)
        return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"

    play_time, adv_time = time2int(play_time), time2int(adv_time)
    logs = [list(map(time2int, log.split("-"))) for log in logs]

    times = [0 for _ in range(play_time + 1)]
    for log in logs:
        a, b = log
        times[a] += 1
        times[b] -= 1

    for i in range(len(times) - 1):
        times[i + 1] += times[i]

    result, value = 0, sum(times[:adv_time])
    my_max = value
    for i in range(len(times) - adv_time):
        if my_max < value:
            result, my_max = i, value
        value += times[adv_time + i] - times[i]

    return int2time(result)
