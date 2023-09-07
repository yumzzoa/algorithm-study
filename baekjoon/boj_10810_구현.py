#10810

basket_size, number = map(int, input().split())

basket = [0] * basket_size

for i in range(number):
    start, end, ball = map(int, input().split())
    for i in range(start-1, end):
        basket[i] = ball
        
for ball_number in basket:
    print(ball_number, end=" ")