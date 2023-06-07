def compress(chars):
    write = 0
    count = 0
    prev = None

    for read in range(len(chars)):
        if chars[read] == prev:
            count += 1
        else:
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            chars[write] = chars[read]
            write += 1

            prev = chars[read]
            count = 1

    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1

    return write
chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)  # Output: 6
print(chars[:new_length])  # Output: ["a", "2", "b", "2", "c", "3"]
