import sys
import math
from collections import Counter
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    C=Counter(S)
    M=max(C.values())
    print(N-M)