def evaluate_postfix(expression):
    stack = []  # Create an empty stack

    # Iterate over each character in the expression
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()

expression = "231*+9-"
result = evaluate_postfix(expression)
print(result)
