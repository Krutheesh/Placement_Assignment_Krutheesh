def first_non_repeating_char_index(s):
    char_freq = {}

    # Count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    # If no non-repeating character found
    return -1

# Example usage
string = "leetcode"
index = first_non_repeating_char_index(string)
print(index)  # Output: 0 (The first non-repeating character is 'l' at index 0)
