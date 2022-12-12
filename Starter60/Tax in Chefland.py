import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N>100:
        print(N-10)
    else:
        print(N)