def cal_ad(std_start, std_end, times_list):
    total_ad = 0
    for lists in times_list:
        compare_start = lists[0]
        compare_end = lists[1]
        
        start = max(std_start, compare_start)
        end = min(std_end, compare_end)
        
        if end-start < 0:
            continue
        else:
            total_ad += end-start
    return total_ad
        
def make_time(time):
    return int(time[0])*3600 + int(time[1])*60 + int(time[2])

def decode_time(time):
    a = time // 3600
    b = (time-a*3600) // 60
    c = time-b*60-a*3600
    return ':'.join([str(a).zfill(2),str(b).zfill(2),str(c).zfill(2)])

def solution(play_time, adv_time, logs):
    answer = ''
    
    times_list = []
    start_time = 100*3600
    
    play = make_time(play_time.split(':'))
    adv = make_time(adv_time.split(':'))
    
    
    if play_time == adv_time:
        return "00:00:00"
    
    for i in range(len(logs)):
        times = logs[i].split('-')
        
        lists1 = times[0].split(':')
        lists2 = times[1].split(':')
        
        start_ = make_time(lists1)
        end_ = make_time(lists2)
        
        times_list.append([start_, end_])
        
    times_list = sorted(times_list, key=lambda x:x[0])
    max_ad = -1
    max_start_time = 3600*100
    for i in range(len(times_list)):
        start = times_list[i][0]
        # 기준 start, end 만들기
        std_start = start
        std_end = start+adv
        if std_end > play:
            std_end = play
        
        # 시간 계산하기
        ad = cal_ad(std_start, std_end, times_list)
        if ad > max_ad:
            max_ad = ad
            max_start_time = std_start
        elif ad == max_ad and max_start_time > std_start:
            max_start_time = std_start
    
    return decode_time(max_start_time)