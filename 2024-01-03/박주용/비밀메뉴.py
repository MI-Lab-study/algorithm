import sys

temp = input()

secret = input().split()
user = input().split()

k = 0
for i in range(len(user)):
  m = 0
  for t in range(len(secret)):
    try:
      user_button = user[i+t]
      secret_std = secret[k+t]
      if user_button == secret_std:
        m += 1
      else:
        std = 1
        break
      if m == len(secret):
        std = 0
        print('secret')
        break
      else:
        std = 1
    except:
      break
  if std == 0:
    break
try:
  if std == 1:
    print('normal')
except:
  std = 0

  