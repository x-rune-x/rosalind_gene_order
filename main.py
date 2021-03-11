from itertools import permutations


def get_permutations(n):
    # Create a list of numbers from 1 to n.
    integers = [i for i in range(1, n+1)]

    # Permutations function finds the permutations.
    perms = permutations(integers)

    # Having trouble with permutations object only being usable once. (?) So convert it to list. Can easily grab length
    # in list form as well.
    list_perm = list(perms)
    perm_len = len(list_perm)

    # Rosalind wants the number of permutations listed at the start so create a string beginning with that.
    out_string = f'{perm_len}'
    for perm in list_perm:
        # Rosalind does not want brackets and commas between digits so this nested loop converts every element to a
        # string before adding it to our output string.
        str_conv = ''
        for element in perm:
            str_conv += str(element) + ' '

        out_string += '\n' + str_conv

    output_text = open("solution.txt", "w")
    output_text.write(out_string)
    output_text.close()

    return out_string


solution = get_permutations(7)
print(solution)
