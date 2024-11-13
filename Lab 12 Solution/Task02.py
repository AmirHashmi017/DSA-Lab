network = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited_nodes = set()

def dfs_search(visited_nodes, network, start_node):
    if start_node not in visited_nodes:
        print(start_node, end=" ")
        visited_nodes.add(start_node)
        for adjacent in network[start_node]:
            dfs_search(visited_nodes, network, adjacent)

print("Depth-First Search traversal of the graph:")
dfs_search(visited_nodes, network, '5')
