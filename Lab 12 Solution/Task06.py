from sys import maxsize
from itertools import permutations

num_vertices = 4

def tsp_solver(matrix, start):
    vertices = [i for i in range(num_vertices) if i != start]
    shortest_path_cost = maxsize
    routes = permutations(vertices)
    
    for route in routes:
        path_cost = 0
        current_vertex = start
        
        for next_vertex in route:
            path_cost += matrix[current_vertex][next_vertex]
            current_vertex = next_vertex
        
        path_cost += matrix[current_vertex][start]
        shortest_path_cost = min(shortest_path_cost, path_cost)
    
    return shortest_path_cost

if __name__ == "__main__":
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_vertex = 0
    print("Minimum path cost:", tsp_solver(matrix, start_vertex))
