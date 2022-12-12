import sys
import math
from collections import Counter
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    a=S.count('0')
    b=S.count('1')
    if a>b:
        print(b+1)
    elif b>a:
        print(a+1)
    elif a==b:
        print(0)
    