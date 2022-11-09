INF = int(1e9)
n, m = map(int, input().split()) #회사의 개수 n, 경로의 개수 m

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for t in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

# for i in range(n+1):
#     for j in range(n+1):
#         print(graph[i][j], end = " ")
#     print()