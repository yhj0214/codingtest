

n, m = map(int, input().split())
narr = list(map(int, input().split()))
start = 0
end = max(narr)
result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in narr:
        if i > mid:
            total = total + i - mid
    if total == m:
        answer = mid
        break
    elif total < m:
        end = mid-1
    else:
        start = mid +1
        answer = mid
print(answer)

        