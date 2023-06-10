def count_consonants(string):
    string = string.lower()
    return count_consonants_recursive(string)

def count_consonants_recursive(string):
    if string == "":
        return 0
    elif string[0].isalpha() and string[0] not in "aeiou":
        return 1 + count_consonants_recursive(string[1:])
    else:
        return count_consonants_recursive(string[1:])

input_string = input("Enter a string: ")
consonant_count = count_consonants(input_string)
print("Total number of consonants:", consonant_count)
