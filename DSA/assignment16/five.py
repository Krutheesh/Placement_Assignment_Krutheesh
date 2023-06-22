def reverse_number(number):
    number_str = str(number)
    stack = []

    # Push each character onto the stack
    for char in number_str:
        stack.append(char)

    reversed_number_str = ''

    # Pop each character from the stack and append it to the reversed number string
    while stack:
        reversed_number_str += stack.pop()

    reversed_number = int(reversed_number_str)

    return reversed_number
number = 365
reversed_number = reverse_number(number)
print(reversed_number)  # 563

number = 6899
reversed_number = reverse_number(number)
print(reversed_number)  # 9986
