n = int(input())
result = 0
count = 0
peoples = list(map(int, input().split()))

for people in peoples:
    count += 1
    if count >= people:
        count = 0
        result +=1
print(result)