def warshall(adj_matrix: list[list[int]]):
    order = len(adj_matrix)
    for k in range(order):
        for i in range(order):
            for j in range(order):
                adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])
    return adj_matrix