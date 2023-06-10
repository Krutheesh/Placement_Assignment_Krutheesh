def print_subsets(string):
    subsets = []
    generate_subsets(string, "", 0, subsets)
    print(subsets)

def generate_subsets(string, current_subset, index, subsets):
    if index == len(string):
        subsets.append(current_subset)
        return

    generate_subsets(string, current_subset, index + 1, subsets)
    generate_subsets(string, current_subset + string[index], index + 1, subsets)
print_subsets('abc')
print_subsets('abcd')