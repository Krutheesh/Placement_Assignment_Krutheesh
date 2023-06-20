def reverse_stack(stack):
    if len(stack) <= 1:
        return stack

    # Pop an element from the stack
    element = stack.pop()

    # Recursively reverse the remaining stack
    reversed_stack = reverse_stack(stack)

    # Insert the popped element at the bottom of the reversed stack
    reversed_stack.insert(0, element)

    return reversed_stack
stack = [3, 2, 1, 7, 6]
reversed_stack = reverse_stack(stack)
print(reversed_stack)
