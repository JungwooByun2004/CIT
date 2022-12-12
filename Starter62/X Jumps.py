import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a>=b:
        print(a//b + a%b)
    else:
        print(a)