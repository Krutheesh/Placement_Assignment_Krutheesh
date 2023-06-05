def firstUniqChar(s):
    char_count = {}
    

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

   
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

   
    return -1

# Example 1
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

# Example 2
s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

# Example 3
s = "aabb"
print(firstUniqChar(s))  # Output: -1
