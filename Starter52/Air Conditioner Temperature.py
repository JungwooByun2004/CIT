import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    if a>b or b<c:
        print("NO")
    else:
        print("YES")