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
        if current not in visited:
            print(current,end=" ")
            visited.append(current)
            for neighbours in graph[current]:
                if(neighbours not in visited):
                    DFSStack.append(neighbours)
        

#Driver
print("DFS of Graph: ")
DFS(graph,visited,'5')