#3052

list = []

for i in range(10):
    a = int(input())
    b = a % 42
    list.append(b)

s = set(list)
print(len(s))
