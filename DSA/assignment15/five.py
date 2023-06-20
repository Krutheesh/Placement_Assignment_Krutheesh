def reverse_string(string):
    stack = []  # Create an empty stack

    # Push each character onto the stack
    for char in string:
        stack.append(char)

    reversed_string = ""

    # Pop each character from the stack and concatenate them
    while stack:
        reversed_string += stack.pop()

    return reversed_string
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)
