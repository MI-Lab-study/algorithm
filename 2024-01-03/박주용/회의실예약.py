import sys
N,M = map(int, input().split())

room_info = {}
room_name_ls = [] 
start_time = list(range(9, 18))

for i in range(N):
  room_name = input()
  room_name_ls.append(room_name)
  room_info[room_name+'_start'] = start_time.copy()
  room_info[room_name+'_fin'] = []

room_name_ls.sort()

for i in range(M):
  room_name, starts, ends = map(str, input().split())
  starts = int(starts)
  ends = int(ends)
  start_ls = room_info[room_name+'_start']

  for i in range(ends-starts):
    try:
      start_ls.pop(start_ls.index(starts+i))
    except:
      continue
  room_info[room_name+'_start'] = start_ls
  
split = "-----"


for i in range(N):
  avail = []
  name = room_name_ls[i]
  room_starts = room_info[name+'_start']

  k = 0
  for num in room_starts:
    start_std = num - k
    end_std = num + 1
    if end_std in room_starts:
      k += 1
      continue
    else:
      if start_std == 9:
        start_std = '09'
      avail.append(str(start_std)+'-'+str(end_std))
      k = 0
  room_info[name+'_fin'] = avail
  
m = 0
for name in room_name_ls:
  print('Room '+name+":")
  fins = room_info[name+'_fin']
  if len(fins) == 0:
    print('Not available')
  else:
    print(str(len(fins))+' available:')
    for available in fins:
      print(available)
  if m != len(room_name_ls)-1:
    print(split)
    m += 1