def isValid(s):
    stack = []

    for char in s:
        if char == '(' or char == '*':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    count = 0
    while stack:
        if stack.pop() == '(':
            if count == 0:
                return False
            count -= 1
        else:
            count += 1

    return True
s = "()"
result = isValid(s)
print(result)  # Output: True
