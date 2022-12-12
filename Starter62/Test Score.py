import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    if c/b<=c and c%b==0:
        print("yes")
    else:
        print("No")