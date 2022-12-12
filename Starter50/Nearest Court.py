import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    A=abs((X-Y)/2)
    print(math.ceil(A))