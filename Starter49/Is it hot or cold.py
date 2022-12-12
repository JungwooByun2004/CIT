import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N>20:
        print('HOT')
    else:
        print('COLD')