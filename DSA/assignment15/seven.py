class MinStack:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val):
        self.data_stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.data_stack:
            return

        popped = self.data_stack.pop()

        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        if not self.data_stack:
            return -1

        return self.data_stack[-1]

    def getMin(self):
        if not self.min_stack:
            return -1

        return self.min_stack[-1]
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2
