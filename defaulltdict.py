tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

from collections import defaultdict
from collections import deque

d={}

d=defaultdict(deque)
for task, server, b in tasks:
    if b==True:
        d[server].appendleft(task)
    else:
        d[server].append(task)
print(d)