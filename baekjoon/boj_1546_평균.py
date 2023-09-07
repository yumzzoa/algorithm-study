#1546

test_count = int(input())

score = list(map(int, input().split()))

best_score = max(score)

for i in range(test_count):
    score[i] = score[i] / best_score * 100

print(sum(score) / test_count)