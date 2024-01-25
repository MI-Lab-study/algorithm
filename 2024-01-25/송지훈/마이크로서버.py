import math

test_case_counts = int(input())
need_servers = []

for i in range(test_case_counts):
    servers = 0

    N = int(input())  # test case의 길이
    test_case = list(map(int, input().split()))

    test_case = sorted(test_case)

    while test_case:
        t = test_case[-1]

        if t <= 600:
            break
        else:
            test_case.pop()
            servers += 1

    len600 = N - servers  # 600이하의 개수

    # test_case에 600이하만 모아놓음
    len300 = 0      # 300의 개수
    
    for t in test_case:
        if t > 300:
            break
        else:
            len300 += 1

    lennot300 = len600 - len300      # 600이하 중 300이 아닌 것의 개수

    test_not_300_case = test_case[len300:]

    start = 0
    end = lennot300 - 1

    
    while lennot300>1:
        if test_not_300_case[start] + test_not_300_case[end] > 900:
            if len300 > 0:     # 300이랑 같이 한 server에 들어가거나 혼자 써야함
                len300 -= 1

            end -= 1
            lennot300 -= 1
            servers += 1
                
        else:
            start += 1
            end -= 1
            lennot300 -= 2

            servers += 1
    else:
        if lennot300 == 1:
            servers += 1
            servers += math.ceil((len300-1)/3)
        else:
            servers += math.ceil(len300/3)
    
    need_servers.append(servers)

for n in need_servers:
    print(n)
