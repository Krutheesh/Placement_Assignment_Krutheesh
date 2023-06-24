def reveal_cards_increasing_order(deck):
    n = len(deck)
    indices = list(range(n))
    indices.sort(key=lambda i: deck[i])
    result = [0] * n
    revealed = [False] * n
    i = 0

    for card in sorted(deck):
        while revealed[indices[i]]:
            i = (i + 1) % n

        result[indices[i]] = card
        revealed[indices[i]] = True
        i = (i + 1) % n

    return result
deck = [1, 1000]
output = reveal_cards_increasing_order(deck)
print(output)  # Output: [1, 1000]
