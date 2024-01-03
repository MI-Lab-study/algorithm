import sys

input = sys.stdin.readline

N = int(input())

my_map = []
for _ in range(N):
    my_map += [list(input().rstrip())]

result = []
for i in range(N):
    for j in range(N):
        if my_map[i][j] == "1":
            my_map[i][j] = "0"
            answer = 1
            my_next = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]

            while my_next:
                a, b = my_next.pop()
                if a >= 0 and a < N and b >= 0 and b < N and my_map[a][b] == "1":
                    my_map[a][b] = "0"
                    answer += 1
                    my_next += [(a + 1, b), (a, b + 1), (a - 1, b), (a, b - 1)]
            result.append(answer)

print(len(result))
print("\n".join(map(str, sorted(result))))
