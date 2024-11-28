<<<<<<< HEAD
import copy
from heapq import heappush, heappop

size = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

class MinHeap:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        heappush(self.data, item)
    
    def pop(self):
        return heappop(self.data)
    
    def is_empty(self):
        return not self.data

class PuzzleNode:
    def __init__(self, parent, matrix, empty_pos, heuristic_cost, depth):
        self.parent = parent
        self.matrix = matrix
        self.empty_pos = empty_pos
        self.heuristic_cost = heuristic_cost
        self.depth = depth
    
    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost

def misplaced_tiles(matrix, goal):
    mismatch = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] and matrix[i][j] != goal[i][j]:
                mismatch += 1
    return mismatch

def create_node(matrix, empty_pos, new_empty_pos, depth, parent, goal):
    new_matrix = copy.deepcopy(matrix)
    x1, y1 = empty_pos
    x2, y2 = new_empty_pos
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    
    heuristic_cost = misplaced_tiles(new_matrix, goal)
    return PuzzleNode(parent, new_matrix, new_empty_pos, heuristic_cost, depth)

def display(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def within_bounds(x, y):
    return 0 <= x < size and 0 <= y < size

def display_path(node):
    if node is None:
        return
    display_path(node.parent)
    display(node.matrix)

def solve_puzzle(start, empty_pos, goal):
    heap = MinHeap()
    root_cost = misplaced_tiles(start, goal)
    root = PuzzleNode(None, start, empty_pos, root_cost, 0)
    heap
=======
import copy
from heapq import heappush, heappop

size = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

class MinHeap:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        heappush(self.data, item)
    
    def pop(self):
        return heappop(self.data)
    
    def is_empty(self):
        return not self.data

class PuzzleNode:
    def __init__(self, parent, matrix, empty_pos, heuristic_cost, depth):
        self.parent = parent
        self.matrix = matrix
        self.empty_pos = empty_pos
        self.heuristic_cost = heuristic_cost
        self.depth = depth
    
    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost

def misplaced_tiles(matrix, goal):
    mismatch = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] and matrix[i][j] != goal[i][j]:
                mismatch += 1
    return mismatch

def create_node(matrix, empty_pos, new_empty_pos, depth, parent, goal):
    new_matrix = copy.deepcopy(matrix)
    x1, y1 = empty_pos
    x2, y2 = new_empty_pos
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    
    heuristic_cost = misplaced_tiles(new_matrix, goal)
    return PuzzleNode(parent, new_matrix, new_empty_pos, heuristic_cost, depth)

def display(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def within_bounds(x, y):
    return 0 <= x < size and 0 <= y < size

def display_path(node):
    if node is None:
        return
    display_path(node.parent)
    display(node.matrix)

def solve_puzzle(start, empty_pos, goal):
    heap = MinHeap()
    root_cost = misplaced_tiles(start, goal)
    root = PuzzleNode(None, start, empty_pos, root_cost, 0)
    heap
>>>>>>> d07c946dcb53b95415258cd54771b79c5a9b122e
