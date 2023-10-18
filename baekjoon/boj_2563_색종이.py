#2563

n = int(input())

white_paper = [[0] * 100 for i in range(100)]

for i in range(n):
    x, y = list(map(int, input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            white_paper[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if white_paper[i][j] == 1:
            count += 1

print(count)
