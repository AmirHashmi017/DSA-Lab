graph_data = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

explored = []
queue_list = []

def bfs_search(explored, graph_data, start_node):
    explored.append(start_node)
    queue_list.append(start_node)
    
    while queue_list:
        current = queue_list.pop(0)
        print(current, end=" ")
        
        for adjacent in graph_data[current]:
            if adjacent not in explored:
                explored.append(adjacent)
                queue_list.append(adjacent)

print("Breadth-First Search traversal of the graph:")
bfs_search(explored, graph_data, '5')
