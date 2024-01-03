import sys

input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split())

secret = input().rstrip()
is_secret = input().rstrip()

print("secret" if secret in is_secret else "normal")
