import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    if a%2==0 and b%2==0 and c%2==0:
        print("No")
    elif a%2==1 and b%2==1 and c%2==1:
        print("No")
    else:
        print("Yes")