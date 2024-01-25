import sys
from collections import deque
H,W = map(int, input().split())


image = []
image.append(['-1' for x in range(W+2)])
for _ in range(H):
    k = list(map(str, (input().split())))
    k = ['-1'] + k + ['-1']
    image.append(k)
image.append(['-1' for x in range(W+2)])

Q = int(input())

temp_list = []
temp_list = deque(temp_list)
for _ in range(Q):
    x,y,change_color = map(int, input().split())
    std_color = str(image[x][y])
    change_color = str(change_color)
    temp_list.append((x,y))
    image[x][y] = change_color
    while temp_list:
        x,y = temp_list.pop()
        if image[x+1][y] == std_color:
            temp_list.append((x+1,y))
            image[x+1][y] = change_color
        if image[x-1][y] == std_color:
            temp_list.append((x-1,y))
            image[x-1][y] = change_color
        if image[x][y+1] == std_color:
            temp_list.append((x,y+1))
            image[x][y+1] = change_color
        if image[x][y-1] == std_color:
            temp_list.append((x,y-1))
            image[x][y-1] = change_color
output = [' '.join(x[1:-1]) for x in image[1:-1]]
sys.stdout.write('\n'.join(output))

