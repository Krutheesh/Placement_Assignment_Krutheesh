def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
s = "Let's take LeetCode contest"
print(reverse_words(s))
