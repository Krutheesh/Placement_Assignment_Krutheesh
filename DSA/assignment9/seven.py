def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  # backtrack

def printPermutations(S):
    s = list(S)
    n = len(s)
    permute(s, 0, n - 1)
printPermutations("ABC")
# Output: ABC, ACB, BAC, BCA, CBA, CAB
print('-------')
printPermutations("XY")
# Output: XY, YX
