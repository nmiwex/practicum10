def create_shift_table(pattern):
    """
    Creates a shift table for the Boyer-Moore algorithm
    :param pattern: substring
    :return: shift table
    """
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = max(1, len(pattern) - i - 1)

    return table


def sub_find(string: str, sub: str, start=0, end=None):
    """
    returns the index of the first occurrence of a substring in a string
    using the Boyer-Moore algorithm
    """
    shift_table = create_shift_table(sub)

    if end is None:
        end = len(string)

    cur_ind = start + len(sub) - 1
    while cur_ind < end:
        i = 0

        while i < len(sub) and string[cur_ind - i] == sub[len(sub) - 1 - i]:
            i += 1

        if i == len(sub):
            return cur_ind - len(sub) + 1

        last_char = string[cur_ind]
        shift = shift_table.get(last_char, len(sub))
        cur_ind += shift

    return -1


def find_all(string: str, sub: str) -> str:
    """
    finds all occurrences of a substring in a string
    """
    all_ind = []
    start = 0

    while True:
        ind = sub_find(string, sub, start, len(string))
        if ind == -1:
            break

        all_ind.append(str(ind))
        start = ind + 1

    return ', '.join(all_ind)