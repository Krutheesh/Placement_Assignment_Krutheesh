def count_contiguous_substrings(S):
    count = 0
    for i in range(len(S)):
        count += count_substrings(S, i, i)
    return count

def count_substrings(S, start, end):
    if start < 0 or end >= len(S) or S[start] != S[end]:
        return 0
    return 1 + count_substrings(S, start - 1, end + 1)
print(count_contiguous_substrings("abc"))  # Output: 3
print(count_contiguous_substrings("aabca"))  # Output: 5
