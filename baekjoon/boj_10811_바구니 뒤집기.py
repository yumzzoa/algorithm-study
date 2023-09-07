#10811

basket_size, order = map(int, input().split())

basket = [str(i) for i in range(1, basket_size+1)]

for i in range(order):
    start, end = map(int, input().split())
    result = basket[start-1:end]
    result.reverse()
    basket[start-1:end] = result

print(' '.join(basket))