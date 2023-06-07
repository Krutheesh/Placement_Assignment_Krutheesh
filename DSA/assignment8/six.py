def findAnagrams(s, p):
    indices = []

    p_freq = {}
    window_freq = {}

    for c in p:
        p_freq[c] = p_freq.get(c, 0) + 1

    left, right = 0, 0
    while right < len(s):
        window_freq[s[right]] = window_freq.get(s[right], 0) + 1

        if right - left + 1 > len(p):
            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            left += 1

        if window_freq == p_freq:
            indices.append(left)

        right += 1

    return indices
s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
print(indices)  # Output: [0, 6]
