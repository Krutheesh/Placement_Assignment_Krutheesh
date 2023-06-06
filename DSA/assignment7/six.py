def can_shift_string(s, goal):
    if len(s) != len(goal):
        return False

    # Concatenate s with itself
    shifted_string = s + s

    if goal in shifted_string:
        return True
    else:
        return False
s = "abcde"
goal = "cdeab"
print(can_shift_string(s, goal))
