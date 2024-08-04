def shift_table(pattern: str) -> list[int]:
    shift_table = [len(pattern) for i in range(128)]

    for i in range(len(pattern) - 1):
        shift_table[ord(pattern[i])] = len(pattern) - 1 - i

    return shift_table

def horspool_search(pattern: str, string: str) -> int:
    table = shift_table(pattern)
    m = len(pattern)
    n = len(string)
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and string[i + j] == pattern[j]:
            j -= 1
        
        if j < 0:
            return i
        else:
            i += table[ord(string[i + m - 1])]

    return -1