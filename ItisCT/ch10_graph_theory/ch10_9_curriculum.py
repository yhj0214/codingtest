from collections import deque
import copy
n = int(input())

classtime = [0] * (n+1)
outline = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    classtime[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        outline[i] += 1

def topology_sort():
    sumtime = copy.deepcopy(classtime)
    queue = deque()
    for i in range(1,n+1):
        if outline[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        for j in graph[now]:
            outline[j] -= 1
            sumtime[j] = max(classtime[j], sumtime[now]+classtime[j])
            if outline[j] == 0:
                queue.append(j)
    print(sumtime)

topology_sort()

