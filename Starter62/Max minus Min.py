import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print(max(A,B,C)-min(A,B,C))