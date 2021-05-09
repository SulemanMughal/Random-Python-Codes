from collections import deque
a = ['Suleman', 'Shahid', 'Mehmood', 'Mughal']
queue = deque(a)
queue.append('Yousuf')
queue.append('Babar')
queue.popleft()
queue.popleft()
queue.append('Suleman Shahid Mehmood Mughal')
queue.popleft()
