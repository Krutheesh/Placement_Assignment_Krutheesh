def backspace_compare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    processed_s = process_string(s)
    processed_t = process_string(t)

    return processed_s == processed_t
s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))
