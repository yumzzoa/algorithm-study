#2562

numbers = []

for i in range(9):
    n = int(input())
    numbers.append(n)

print(max(numbers))
print(numbers.index(max(numbers))+1)