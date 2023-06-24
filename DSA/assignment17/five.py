def find_last_person(n, k):
    # Create a list representing the circle of people
    circle = list(range(1, n + 1))

    # Start from the first person
    current = 0

    while len(circle) > 1:
        # Find the k-th person and remove them from the circle
        current = (current + k - 1) % len(circle)
        circle.pop(current)

    # Return the last remaining person
    return circle[0]
n = 5
k = 2
output = find_last_person(n, k)
print(output)  # Output: 3