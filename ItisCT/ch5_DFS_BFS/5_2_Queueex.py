from collections import deque as dq

queue = dq()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()
queue.append(1)
queue.append(4)

queue.popleft()

print(queue)
queue.reverse()
print(queue)