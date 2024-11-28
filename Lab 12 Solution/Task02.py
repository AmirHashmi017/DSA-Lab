graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
visited=[]
DFSStack=[]
def DFS(graph,visited,startnode):
    DFSStack.append(startnode)
    while(DFSStack):
        current=DFSStack.pop()
        if(current not in visited):
            visited.append(current)
            print(current,end=" ")
            for neighbours in graph[current]:
                if(neighbours not in visited):
                    DFSStack.append(neighbours)
            


print("Depth-First Search traversal of the graph:")
DFS(graph,visited, '5')
