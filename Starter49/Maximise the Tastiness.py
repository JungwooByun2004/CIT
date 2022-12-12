import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A,B,C,D = map(int, input().split())
    print(max(A,B)+max(C,D))