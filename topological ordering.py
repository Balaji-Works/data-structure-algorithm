def dfs(node, visited, stack, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, graph)
    stack.append(node)

def topological_sort(graph, vertices):
    visited = [False] * vertices
    stack = []

    for i in range(vertices):
        if not visited[i]:
            dfs(i, visited, stack, graph)

    print("Topological Order:", stack[::-1])


# Example graph
graph = [
    [],        # 0
    [3],       # 1 → 3
    [3],       # 2 → 3
    [4],       # 3 → 4
    []         # 4
]

topological_sort(graph, 5)
