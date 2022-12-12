import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a*2>b*5:
        print("Chocolate")
    elif a*2<b*5:
        print("Candy")
    else:
        print("Either")