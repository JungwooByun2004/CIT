import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,X,Y,A,B = map(int, input().split())
    if X/A > Y/B:
        print("DIESEL")
    elif X/A < Y/B:
        print("PETROL")
    elif X/A == Y/B:
        print("ANY")