import heapq as hq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

v, e = map(int, input().split())
parent = [0] * (v+1)

result = 0
edges = []

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    hq.heappush(edges, (cost, a, b))

for _ in range(e):
    cost, a, b = hq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)