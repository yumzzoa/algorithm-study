#5597

student = [i for i in range(1, 31)]

for i in range(28):
    number = int(input())
    student.remove(number)

print(min(student))
print(max(student))
