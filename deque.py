from collections import deque 



q = deque()


q.append(5)
q.append(6)
q.append(7)
q.append(8)

print(q)

q.pop()

print(q)



q.append([8,9,10])

print(q)


q.pop()

q.appendleft(5)

print(q)