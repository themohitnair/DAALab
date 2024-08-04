def shift_table(pattern: str) -> list[int]:
    table = [len(pattern) for i in range(128)]
    for i in range(len(pattern) - 1):
        table[ord(pattern[i])] = len(pattern) - i - 1
    return table

def horspool_search(pattern: str, string: str) -> int:
    table = shift_table(pattern)
    m = len(pattern)
    n = len(string)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == string[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            i += table[ord(string[i + m - 1])]
    return -1