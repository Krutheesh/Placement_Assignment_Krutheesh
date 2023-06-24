class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FrontMiddleBackQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushFront(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pushMiddle(self, val):
        if self.size == 0:
            self.pushFront(val)
            return

        middle = self.size // 2
        curr = self.head
        for _ in range(middle):
            curr = curr.next

        new_node = ListNode(val)
        new_node.prev = curr
        new_node.next = curr.next
        if curr.next is not None:
            curr.next.prev = new_node
        curr.next = new_node

        if self.size % 2 == 1:
            self.tail = self.tail.next

        self.size += 1

    def pushBack(self, val):
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def popFront(self):
        if self.size == 0:
            return -1

        val = self.head.val
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

        return val

    def popMiddle(self):
        if self.size == 0:
            return -1

        middle = self.size // 2
        curr = self.head
        for _ in range(middle - 1):
            curr = curr.next

        val = curr.next.val
        if curr.next.next is not None:
            curr.next = curr.next.next
            curr.next.prev = curr
        else:
            curr.next = None
            self.tail = curr

        if self.size % 2 == 1:
            self.tail = self.tail.prev

        self.size -= 1

        return val

    def popBack(self):
        if self.size == 0:
            return -1

        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1

        return val
q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
print(q.popFront())   # Output: 1
print(q.popMiddle())  # Output: 4
print(q.popMiddle())  # Output: 3
print(q.popBack())    # Output: 2
print(q.popFront())   # Output: -1
