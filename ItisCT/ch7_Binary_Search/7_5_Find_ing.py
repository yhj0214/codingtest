def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return print("yes", end = ' ')
        elif array[mid] >= target:
            end = mid-1
        else:
            start = mid+1
    return print("no", end = ' ')

n = int(input())
narr = list(map(int, input().split()))
narr.sort()
m = int(input())
marr = list(map(int, input().split()))

for i in marr:
    answer = binary_search(narr, i, 0, n-1)

