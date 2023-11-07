#11005

num, step = map(int, input().split())

box = []
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    if num == 0:
        break
    box.append(alpha[num % step])
    num = num // step

box.reverse()
print("".join(box))