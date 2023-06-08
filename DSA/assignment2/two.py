def max_candies(candyType):
    unique_types = len(set(candyType))
    max_candy_types = min(len(candyType) // 2, unique_types)
    return max_candy_types
candyType = [1, 1, 2, 2, 3, 3]
max_types = max_candies(candyType)
print(max_types)
