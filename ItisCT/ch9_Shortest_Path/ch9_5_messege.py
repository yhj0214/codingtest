import heapq as hq
INF = int(1e9)
n, m, c = map(int, input().split()) # 도시개수 n, 통로수 m, 메시지를 보내려는 도시c

graph = [[] for i in range(n+1)]
distance = [INF] *(n+1)

for _ in range(m):
    x, y, z = map(int, input().split()) # x->y z시간 소요
    graph[x].append((y,z))



def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0
    for i in graph[start]:
        graph[i[0]] = i[1]

    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0

max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)

