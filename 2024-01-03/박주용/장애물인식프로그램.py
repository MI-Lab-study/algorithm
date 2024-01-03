import sys


N = int(input())
dicts = {}
for i in range(N):
  row = input()
  for j in range(N):
    dicts[str(i)+','+str(j)] = row[j]

num_ls = []
t = 0
u = 0
for i in range(N):
  for j in range(N):
    temp_ls = []
    if dicts[str(i)+','+str(j)] == 0:
      continue
    else:
      temp_ls.append(str(i)+','+str(j))
      k = 1
      while True:
        k = len(temp_ls)
        for o in range(len(temp_ls)):
          up = int(temp_ls[o][0])-1
          down = int(temp_ls[o][0])+1
          right = int(temp_ls[o][2])+1
          left = int(temp_ls[o][2])-1
          try:
            if dicts[str(up)+','+str(temp_ls[o][2])] == 1 and str(up)+','+str(temp_ls[o][2]) not in temp_ls:
              temp_ls.append(str(up)+','+str(temp_ls[o][2]))
          except:
            u = 0
          try:
            if dicts[str(down)+','+str(temp_ls[o][2])] == 1 and str(down)+','+str(temp_ls[o][2]) not in temp_ls:
              temp_ls.append(str(down)+','+str(temp_ls[o][2]))
          except:
            u = 0
          try:
            if dicts[str(temp_ls[o][0])+','+str(right)] == 1 and str(temp_ls[o][0])+','+str(right) not in temp_ls:
              temp_ls.append(str(temp_ls[o][0])+','+str(right))
          except:
            u = 0
          try:
            if dicts[str(temp_ls[o][0])+','+str(left)] == 1 and str(temp_ls[o][0])+','+str(left) not in temp_ls:
              temp_ls.append(str(temp_ls[o][0])+','+str(left))
          except:
            u = 0
        if len(temp_ls) == k:
          break

      num_ls.append(len(temp_ls))  
      t += 1
      
      for temp in temp_ls:
        dicts[temp] = 0
num_ls.sort()
print(t)
for num in num_ls:
  print(num)
        