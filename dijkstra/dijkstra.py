import heapq

def dijkstra(mat: list[list[int]], source: int):
    n = len(mat)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    min_heap = [(0, source)]

    while min_heap:
        init_dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        for v in range(n):
            if visited[v] == False and mat[u][v] > 0:
                new_dist = dist[u] + mat[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (dist[v], v))

    return dist

adj_matrix = [
    [0, 10, 0, 0, 0, 0],
    [10, 0, 5, 0, 0, 0],
    [0, 5, 0, 20, 1, 0],
    [0, 0, 20, 0, 2, 5],
    [0, 0, 1, 2, 0, 3],
    [0, 0, 0, 5, 3, 0]
]

print(dijkstra(adj_matrix, 0))
