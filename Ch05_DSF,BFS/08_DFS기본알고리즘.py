graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
]

l_visited = [False] * 9

def dfs(graph, visiting_node, list_visited):
    list_visited[visiting_node] = True
    print(visiting_node, end=' ')
    
    for i in graph[visiting_node]:
        if not list_visited[i]: dfs(graph, i, list_visited)

dfs(graph, 1, l_visited)