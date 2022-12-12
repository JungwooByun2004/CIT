import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    R = list(input())
    count=0
    for i in range(N):
        if S[i]!=R[i]:
            count+=1
    if count%2==0:
        print(1)
    else:
        print(0)
