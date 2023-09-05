#15552

T = int(input())

import sys

for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)