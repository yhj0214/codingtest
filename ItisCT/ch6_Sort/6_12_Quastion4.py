n, k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=False)
b.sort(reverse=True)

for i in range(n):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
        k = k -1
    if k ==0:
        break

print(sum(a))