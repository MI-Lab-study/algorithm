def solution(play_time, adv_time, logs):
    answer = ''
    HH, MM, SS = map(int, play_time.split(':'))
    play_time = HH * 3600 + MM * 60 + SS
    HH, MM, SS = map(int, adv_time.split(':'))
    adv_time = HH * 3600 + MM * 60 + SS
    startlist = []
    finishlist = []
    
    for ts in logs:
        start, end = ts.split('-')
        start_hours, start_minutes, start_seconds = map(int, start.split(':'))
        end_hours, end_minutes, end_seconds = map(int, end.split(':'))
        start_total_seconds = start_hours * 3600 + start_minutes * 60 + start_seconds
        end_total_seconds = end_hours * 3600 + end_minutes * 60 + end_seconds
        startlist.append(start_total_seconds)
        finishlist.append(end_total_seconds)
    
    adv_list=logs
    for idx, i in enumerate(startlist):
        adv_list[idx] = 0
        for j in startlist:
            if i + adv_time >= j:
                adv_list[idx] += 1
        for p in finishlist:
            if i - adv_time <= p:
                adv_list[idx] += 1
    print(adv_list)
    max_value = max(adv_list)
    max_indices = [index for index, value in enumerate(adv_list) if value == max_value]
    answer = min([startlist[idxx] for idxx in max_indices])
    hours = answer // 3600
    remaining_seconds = answer % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # HH:MM:SS 형식으로 출력
    answer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    if adv_time+min(startlist) >= play_time :
        answer = "00:00:00"
    else :
        answer = answer
    return answer