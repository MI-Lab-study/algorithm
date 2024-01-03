import sys

kay = [0,0,0,0,0,0,0]
zero = [1,1,1,0,1,1,1]
one = [0,0,1,0,0,1,0]
two = [1,0,1,1,1,0,1]
three = [1,0,1,1,0,1,1]
four = [0,1,1,1,0,1,0]
five = [1,1,0,1,0,1,1]
six = [1,1,0,1,1,1,1]
seven = [1,1,1,0,0,1,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,1,0,1,1]
num_dicts = {'0':zero, '1':one, '2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine,'k':kay}
T = int(input())

for _ in range(T):
  A, B = map(str, input().split())
  leng_A = len(A)
  leng_B = len(B)
  if leng_A != 5:
    for _ in range(5-leng_A):
      A = 'k' + A
  if leng_B != 5:
    for _ in range(5-leng_B):
      B = 'k' + B
      
  std_num = 0
  for i in range(5):
    check_a = A[i]
    check_b = B[i]
    check_a_ls = num_dicts[check_a]
    check_b_ls = num_dicts[check_b]
    for j in range(7):
      if check_a_ls[j] != check_b_ls[j]:
        std_num += 1
  print(std_num)