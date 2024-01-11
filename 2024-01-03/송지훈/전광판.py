#def sums(x):
#    N = [int(i) for i in x]

#    return sum(N)


num_dict = {"0": 0b1110111, "1": 0b0000011, "2": 0b0111110, "3": 0b0011111, "4": 0b1001011, "5": 0b1011101, "6": 0b1111101, "7": 0b1010011, "8": 0b1111111, "9": 0b1011111}

num_test_case = int(input('몇 개의 테스트 케이스를 입력 받을 것인가요: '))

for _ in range(num_test_case):
    input_test_case = input('테스트 케이스를 입력해주세요: ').split(' ')

    start = input_test_case[0]
    end = input_test_case[1]

    # start가 반드시 크도록 설정
    if int(start) < int(end):
        start, end = end, start

    M = len(start)
    m = len(end)

    k = 0

    for i in range(m, 0, -1):
        s = num_dict[start[-i]]
        e = num_dict[end[-i]]

        k += bin(s ^ e)[2:].count('1')        # xor  '0b~'

    if M != m:
        for x in start[:-m]:
            k += bin(num_dict[x])[2:].count('1')    # 이 경우 앞의 0들이 생략될 수 있는데 어차피 1의 개수를 세는거라 상관은 없음

    print(k)
