import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if a-b>c-d:
        print("Second")
    elif a-b<c-d:
        print("First")
    elif a-b==c-d:
        print("Any")