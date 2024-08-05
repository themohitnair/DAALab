from collections import deque

def bfs(mat: list[int], source: int):
    n = len(mat)
    queue = deque([source])
    visited = [False] * n
    visited[source] = True
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for i in range(n):
            if mat[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    
    return result