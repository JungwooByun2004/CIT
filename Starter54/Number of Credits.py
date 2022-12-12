import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c= map(int, input().split())
    print(4*a+2*b)