def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    mismatch = []
    positions = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatch.append((s[i], goal[i]))
            positions.append(i)

    if len(mismatch) != 2:
        return False

    c1, c2 = mismatch[0], mismatch[1]
    p1, p2 = positions[0], positions[1]

    return c1[0] == c2[1] and c1[1] == c2[0] and p1 != p2
print(buddyStrings("ab",'ba'))