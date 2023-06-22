from queue import Queue

def check_queue_order(queue):
    n = queue.qsize()
    stack = []
    second_queue = Queue()
    expected = 1

    while not queue.empty():
        front = queue.get()

        if front == expected:
            second_queue.put(front)
            expected += 1
        else:
            if stack and stack[-1] == expected:
                second_queue.put(stack.pop())
                expected += 1

            stack.append(front)

    while stack:
        if stack[-1] == expected:
            second_queue.put(stack.pop())
            expected += 1
        else:
            return "No"

    for i in range(1, n+1):
        if second_queue.get() != i:
            return "No"

    return "Yes"
queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
result = check_queue_order(queue)
print(result)  # Yes
