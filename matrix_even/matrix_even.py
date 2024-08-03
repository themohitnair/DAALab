def mat_even(mat: list[list[int]]) -> list[int]:
    m = len(mat)
    n = len(mat[0])
    e_nos = []
    for i in range(m):
        for j in range(n):
            if (mat[i][j] % 2) == 0:
                e_nos.append(mat[i][j])
    return e_nos
