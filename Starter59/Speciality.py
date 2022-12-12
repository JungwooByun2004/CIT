import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    if a>b>c:
        print("Setter")
    elif a>c>b:
        print("Setter")
    elif b>a>c:
        print("Tester")
    elif b>c>a:
        print("Tester")
    elif c>a>b:
        print("Editorialist")
    elif c>b>a:
        print("Editorialist")