#2525

A, B = map(int, input().split())
C = int(input())

A = A + C // 60
B = B + C % 60

if B >= 60:
    print((A+1)%24, B % 60)
else:
    print(A%24, B%60)
