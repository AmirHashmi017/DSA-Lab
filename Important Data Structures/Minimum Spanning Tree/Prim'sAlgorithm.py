import heapq

def PrimsMST(NumberofVertices,NumberOfEdges,EdgesList):
    AdjacencyList=[[] for i in range(NumberofVertices)]
    for start,end,weight in EdgesList:
        AdjacencyList[start].append((end,weight))
        AdjacencyList[end].append((start,weight))

        PriorityQueue=[]
        MST=[]
        visited=[False]*NumberofVertices
        MSTWeight=0
        heapq.heappush(PriorityQueue,(0,0,-1))
        while(PriorityQueue):
            weight,start,parent=heapq.heappop(PriorityQueue)
            if(visited[start]==True):
                continue
            MSTWeight+=weight
            visited[start]=True
            if(parent!=-1):
                MST.append((parent,start,weight))
            for startadj,weightadj in AdjacencyList[start]:
                if(visited[startadj]==False):
                    heapq.heappush(PriorityQueue,(weightadj,startadj,start))

    print("Edge \t   Weight")
    for start,end,weight in MST:
        print(f"{start}---->{end} \t {weight}")

    print(f"TotalWeight: {MSTWeight}")

#Driver
graph = [[0, 1, 2],
             [0, 3, 6], 
             [1, 2, 3],
             [1, 3, 8],  
             [1, 4, 5], 
             [2, 4, 7],  
             [3, 4, 9]] 

V = 5
E = len(graph) 
PrimsMST(V, E, graph)

# Runtime of Prim's Algorithm is O(E log V). Where E is Number Of Edges and V is Numer Of Vertices.



