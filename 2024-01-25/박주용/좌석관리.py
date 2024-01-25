import sys
import math
from collections import defaultdict

N,M,Q = map(int, input().split())

dicts = defaultdict(int)
dicts_coord = {}
output = []


seats = [[0 for i in range(M+2)] for j in range(N+2)]
seats_coord = []


def can(seats, seats_coord):
    if not seats_coord:
        x = 1
        y = 1
        seats[x][y]+= 1
        seats[x+1][y]+= 1
        seats[x-1][y]+= 1
        seats[x][y+1]+= 1
        seats[x][y-1]+= 1
        return True, '(1, 1)', seats

    candi_coord = None
    min_value = -1

    for i in range(1,N+1):
        for j in range(1,M+1):
            if seats[i][j] != 0:
                continue
            std_value = 9999
            for coord_std in seats_coord:
                x_, y_ = coord_std.strip('()').split(',')
                safe_value = ((int(x_)-i)**2+(int(y_)-j)**2)**(1/2)

                if std_value > safe_value:
                    std_value = safe_value
                    
            if std_value > min_value:
                min_value = std_value
                candi_coord = (i,j)
            elif std_value == min_value and i < candi_coord[0]:
                candi_coord = (i,j)
            elif std_value == min_value and (i == candi_coord[0] and j < candi_coord[1]):
                candi_coord = (i,j)

    if not candi_coord:
        return False, '', seats
    else:
        x,y = candi_coord
        seats[x][y]= 1
        seats[x+1][y]=1
        seats[x-1][y]=1
        seats[x][y+1]=1
        seats[x][y-1]=1
        
        return True, f'({candi_coord[0]}, {candi_coord[1]})', seats

def out(seats, candi_coord):
    x,y = candi_coord.strip('()').split(',')
    x = int(x)
    y = int(y)
    seats[x][y]+= -1
    seats[x+1][y]+=-1
    seats[x-1][y]+=-1
    seats[x][y+1]+=-1
    seats[x][y-1]+=-1
    return seats
            
for i in range(Q):
    types, nums = map(str, input().split())
    if types == 'In':
        if dicts[nums] == 1:
            output.append(nums+' already seated.')
            continue
        if dicts[nums] == -1:
            output.append(nums+' already ate lunch.')
            continue
        can_seat, coord, seats = can(seats, seats_coord)
        
        if not can_seat:
            output.append('There are no more seats.')
        else:
            output.append(nums+' gets the seat '+coord+'.')
            dicts[nums] = 1
            seats_coord.append(coord)
            dicts_coord[nums] = coord
    else:
        if dicts[nums] == 0:
            output.append(nums+" didn't eat lunch.")
            continue

        if dicts[nums] == -1:
            output.append(nums+' already left seat.')
            continue

        if dicts[nums] == 1:
            output.append(nums+' leaves from the seat '+dicts_coord[nums]+'.')
            dicts[nums] = -1
            out(seats, dicts_coord[nums])
            seats_coord.remove(dicts_coord[nums])
            
sys.stdout.write('\n'.join(output))