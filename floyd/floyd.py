def floyd(adj_matrix: list[list[int]]):
    order = len(adj_matrix)
    for k in range(order):
        for i in range(order):
            for j in range(order):
                if (adj_matrix[i][k] + adj_matrix[k][j]) < adj_matrix[i][j]:
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
    return adj_matrix