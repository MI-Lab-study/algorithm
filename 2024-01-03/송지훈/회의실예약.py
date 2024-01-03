# 시간은 9~18  총 9개의 구간   0~8

def remain(times):
    # set으로 된 time index가 넘어옴
    times = list(times)
    l = len(times)

    time_dict = {}

    if times[0] != 0:
        time_dict[0] = [0, times[0]]

    for i in range(l - 1):
        if times[i + 1] - times[i] != 1:
            time_dict[len(time_dict)] = [times[i] + 1, times[i + 1]]

    if times[l - 1] != 8:
        time_dict[len(time_dict)] = [times[l - 1] + 1, 9]

    return time_dict


lst = input('').split(' ')
N, M = int(lst[0]), int(lst[1])  # 회의실 개수, 예약된 회의의 수
room_name = {}

for i in range(N):
    room_name[input('')] = set()  # 회의실 이름 입력

for i in range(M):
    meeting_lst = input('').split(' ')  # meeting_room, start, end

    name = meeting_lst[0]
    start, end = int(meeting_lst[1]), int(meeting_lst[2])

    room_name[name] = room_name[name].union(set([i for i in range(start - 9, end - 9)]))  # 사용한 시간대

room_name = dict(sorted(room_name.items()))

for idx, key in enumerate(room_name.keys()):
    room_name[key] = set(sorted(list(room_name[key])))
    print(f'Room {key}:')

    if room_name[key] == set([i for i in range(9)]):
        print('Not available')
    else:
        if room_name[key] != set():
            remain_dict = remain(room_name[key])
            print(f'{str(len(remain_dict))} available:')

            for rkey in remain_dict:
                l = remain_dict[rkey]
                print(f'{l[0] + 9:02d}-{l[1] + 9:02d}')
        else:
            print('1 available:')
            print(f'{9:02d}-{18:02d}')

    if idx != len(room_name) - 1:
        print('-----')