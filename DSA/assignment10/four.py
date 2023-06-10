def calculate_length(string):
    if string == '':
        return 0
    return 1 + calculate_length(string[1:])
print(calculate_length("example"))  # Output: 7
