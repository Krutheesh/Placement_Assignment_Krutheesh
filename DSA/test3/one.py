class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(my_stack.pop())  # Output: 30
print(my_stack.is_empty())  # Output: False

print(my_stack.pop())  # Output: 20
print(my_stack.pop())  # Output: 10
print(my_stack.pop())  # Output: Stack is empty
print(my_stack.is_empty())  # Output: True
