def print_permutations(str):
    permutations = []
    generate_permutations(str, 0, len(str)-1, permutations)
    for permutation in permutations:
        print(permutation, end=' ')

def generate_permutations(str, left, right, permutations):
    if left == right:
        permutations.append(''.join(str))
        return

    for i in range(left, right+1):
        str[left], str[i] = str[i], str[left]
        generate_permutations(str, left+1, right, permutations)
        str[left], str[i] = str[i], str[left]  # Backtrack

string = input("Enter a string: ")
print("Permutations:")
print_permutations(list(string))
