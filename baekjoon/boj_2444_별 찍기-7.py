#2444

n = int(input())

for i in range(1, n):
    print(' ' * (n-i) + '*' * (2*i-1))

for k in range(n, 0, -1):
    print(' ' * (n-k) + '*' * (2*k-1))