class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        if not self.is_empty():
            return self.items[0]

def reverse_k_elements(queue, k):
    if queue.is_empty() or k == 0 or k >= queue.size():
        return queue

    stack = []
    count = 0

    # Dequeue the first k elements and push them onto the stack
    while count < k:
        stack.append(queue.dequeue())
        count += 1

    # Enqueue the elements from the stack back into the queue
    while stack:
        queue.enqueue(stack.pop())

    # Move the remaining elements to the end of the queue
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
k = 3

reversed_queue = reverse_k_elements(queue, k)

# Print the elements in the reversed queue
while not reversed_queue.is_empty():
    print(reversed_queue.dequeue(), end=" ")
