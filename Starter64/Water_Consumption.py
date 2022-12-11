import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N>=2000:
        print("yes")
    else:
        print("no")