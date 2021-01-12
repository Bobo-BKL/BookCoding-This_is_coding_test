from collections import deque

queue = deque()

queue.append(8)
queue.append(1)
queue.append(4)
queue.append(2)
print("팝 :", queue.popleft())
queue.append(0)
queue.append(3)
print("팝 :", queue.popleft())

print(queue)
queue.reverse()
print(queue)