"""If you want to create a queue and a stack, use a deque.

append(x) -> appends to the right side
appendleft(x) -> appends to the left side
pop() -> removes an element from the right side
popleft() -> removes an element from the left side
reverse() -> reverses the elements
clear() -> removes all elements
"""

from collections import deque


deq = deque("abcdefg")
print([item for item in deq])

deq.reverse()
print([item for item in deq])
deq.reverse()

deq.append("h")
print([item for item in deq])