import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N>50:
        print("RIGHT")
    else:
        print("LEFT")