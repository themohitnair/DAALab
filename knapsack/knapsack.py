def knapsack(p: list[int], w: list[int], W) -> int:
    n = len(p)
    V = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                V[i][j] = 0
            elif w[i - 1] <= j:
                V[i][j] = max(V[i - 1][j], p[i - 1] + V[i - 1][j - w[i - 1]])
            else:
                V[i][j] = V[i - 1][j]
    return V[n][W]

print(knapsack([12, 10, 20, 15], [2, 1, 3, 2], 5))