def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    char_map = {}
    used_chars = set()

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if s_char in char_map:
            if char_map[s_char] != t_char:
                return False
        else:
            if t_char in used_chars:
                return False
            char_map[s_char] = t_char
            used_chars.add(t_char)

    return True
s = "egg"
t = "add"
print(isomorphic_strings(s, t))
