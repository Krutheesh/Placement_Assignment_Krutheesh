def delete_middle_element(stack):
    size = len(stack)
    mid_index = size // 2
    count = 0
    temp_stack = []

    while stack:
        if count == mid_index:
            stack.pop()
        else:
            temp_stack.append(stack.pop())

        count += 1

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack
stack = [1, 2, 3, 4, 5]
updated_stack = delete_middle_element(stack)
print(updated_stack)  # [1, 2, 4, 5]

stack = [1, 2, 3, 4, 5, 6]
updated_stack = delete_middle_element(stack)
print(updated_stack)  # [1, 2, 4, 5, 6]
