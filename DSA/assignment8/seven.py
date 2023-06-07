def decodeString(s):
    stack = []

    for c in s:
        if c == ']':
            substring = ''
            while stack[-1] != '[':
                substring += stack.pop()
            stack.pop()  # Pop '['

            count = ''
            while stack and stack[-1].isdigit():
                count += stack.pop()
            count = int(count[::-1])

            stack.append(substring[::-1] * count)

        else:
            stack.append(c)

    return ''.join(stack)

s = "3[a]2[bc]"
decoded = decodeString(s)
print(decoded)  # Output: "aaabcbc"
