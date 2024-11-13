graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited=[]
BFSQueue=[]
def BFS(graph,visited,startnode):
    visited.append(startnode)
    BFSQueue.append(startnode)
    while(BFSQueue):
        current=BFSQueue.pop(0)
        print(current,end=" ")
        for neighbours in graph[current]:
            if(neighbours not in visited):
                visited.append(neighbours)
                BFSQueue.append(neighbours)

print("BFS of Graph is \n")
BFS(graph,visited,'5')

# Runtime for both DFS and BFS is O(V+E)
# Where V is number of vertices (nodes) , and E is number of edges.