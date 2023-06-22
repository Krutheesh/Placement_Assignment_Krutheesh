def count_words_after_destruction(sequence):
    stack = []

    for word in sequence.split():
        if not stack or word != stack[-1]:
            stack.append(word)
        else:
            stack.pop()

    return len(stack)

# Example usage
sequence = "ab aa aa bcd ab"
result = count_words_after_destruction(sequence)
print(result)
