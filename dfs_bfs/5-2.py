# 큐 예제

from collections import deque

#큐 구현을 위해 deque 라이브러리 사용
queue = deque()
queue.append(5)
queue.append(3)
queue.popleft()

print(queue)