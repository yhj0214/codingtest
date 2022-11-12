n, m = map(int, input().split()) # 개수 n, 무게 m
balls = list(map(int,input().split()))
result = 0
for i in range(0, len(balls)):
    for j in range(i, len(balls)):
        if balls[i] != balls[j]:
            result += 1

print(result)



