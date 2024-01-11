'''
N개. 회의실 예약할 것
M개 회의실 예약 힘든것
9 to 6

room, start,  end

only hour
room only eng [:10]

N개의 줄에 이름
3 공백 7
룸 개수 , 룸 예약개수

M개의 줄에 r s t
'''

import sys

num_rooms, num_reservations = map(int, input().split())

rooms = []
reservations = []
# 19를 뒤로 보내고 선언하기.
time_slots = [[1] * 19 for _ in range(num_rooms)]
result_slots = [[] for _ in range(num_rooms)]

for _ in range(num_rooms):
    rooms.append(input())

rooms = sorted(rooms)

for _ in range(num_reservations):
    reservations.append(input().split())

for i in range(num_reservations):
    for j in range(num_rooms):
        if reservations[i][0] == rooms[j]:
            start_time = int(reservations[i][1])
            end_time = int(reservations[i][2])
            for k in range(start_time, end_time):
                time_slots[j][k] = 0

first_index = -1
end_index = -1

for i in range(num_rooms):
    for j in range(9, 18):
        if first_index == -1 and time_slots[i][j] == 1:
            first_index = j
            time_slots[i][j] = 0
        elif first_index != -1 and end_index == -1 and (j + 1 == 18 or time_slots[i][j] == 0):
            if j + 1 == 18:
                end_index = j + 1
            else:
                end_index = j
            time_slots[i][j] = 0
            result_slots[i].append((first_index, end_index))
            first_index = -1
            end_index = -1

for i in range(num_rooms):
    print(f"Room {rooms[i]}:")
    if len(result_slots[i]) == 0:
        print("Not available")
    else:
        print(f"{len(result_slots[i])} available:")
        for j in result_slots[i]:
            if j[0] < 10:
                start_time = f"0{j[0]}"
            else:
                start_time = str(j[0])
            if j[1] < 10:
                end_time = f"0{j[1]}"
            else:
                end_time = str(j[1])
            print(f"{start_time}-{end_time}")
    if i != num_rooms - 1:
        print("-----")



# 방의 수와 예약의 수를 입력으로 받음
num_rooms, num_reservations = map(int, input().split())

# 방 이름, 예약 정보, 시간 슬롯, 결과 슬롯을 저장하기 위한 리스트들
rooms = []
reservations = []
time_slots = [[1] * 19 for _ in range(num_rooms)]
result_slots = [[] for _ in range(num_rooms)]

# 방 이름 입력
for _ in range(num_rooms):
    rooms.append(input())

# 방 이름을 정렬
rooms = sorted(rooms)

# 예약 정보 입력
for _ in range(num_reservations):
    reservations.append(input().split())

# 시간 행렬에서 예약된 시간 슬롯 표시
for i in range(num_reservations):
    for j in range(num_rooms):
        if reservations[i][0] == rooms[j]:
            start_time = int(reservations[i][1])
            end_time = int(reservations[i][2])
            for k in range(start_time, end_time):
                time_slots[j][k] = 0

# 각 방에 대해 가능한 시간 슬롯 찾기
first_index = -1
end_index = -1

for i in range(num_rooms):
    for j in range(9, 18):
        if first_index == -1 and time_slots[i][j] == 1:
            first_index = j
            time_slots[i][j] = 0
        elif first_index != -1 and end_index == -1 and (j + 1 == 18 or time_slots[i][j] == 0):
            if j + 1 == 18:
                end_index = j + 1
            else:
                end_index = j
            time_slots[i][j] = 0
            result_slots[i].append((first_index, end_index))
            first_index = -1
            end_index = -1

# 결과 출력
for i in range(num_rooms):
    print(f"방 {rooms[i]}:")
    if len(result_slots[i]) == 0:
        print("사용 가능한 시간 없음")
    else:
        print(f"{len(result_slots[i])} 개 가능한 시간:")
        for j in result_slots[i]:
            if j[0] < 10:
                start_time = f"0{j[0]}"
            else:
                start_time = str(j[0])
            if j[1] < 10:
                end_time = f"0{j[1]}"
            else:
                end_time = str(j[1])
            print(f"{start_time}-{end_time}")
    if i != num_rooms - 1:
        print("-----")

'''
