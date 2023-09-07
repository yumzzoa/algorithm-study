#10813

bucket_size, ball_change = map(int, input().split())
bucket = [str(i) for i in range(1,bucket_size+1)]
for change in range(ball_change):
    start, end = map(int, input().split())
    bucket[start-1], bucket[end-1] = bucket[end-1], bucket[start-1]

print(' '.join(bucket))