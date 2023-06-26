class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue.dequeue())  # Output: 10
print(my_queue.is_empty())  # Output: False

print(my_queue.dequeue())  # Output: 20
print(my_queue.dequeue())  # Output: 30
print(my_queue.dequeue())  # Output: Queue is empty
print(my_queue.is_empty())  # Output: True
