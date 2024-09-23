#Task 01
def printMatrix(A, starting_index, rows, columns):
    startingrow=starting_index[0]
    startingcolumn=starting_index[1]
    for i in range(startingrow,startingrow+rows,1):
        if(i>=len(A)):
            break
        for j in range(startingcolumn,startingcolumn+columns,1):
            if(j>=len(A[i])):
                break
            print(A[i][j], end=' ')
        print("")

#Driver
# A = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
# printMatrix(A, (2, 2), 2, 3)
#Task 02
def MatAdd(A,B):
    if len(A) != len(B):
        return "Matrices have different number of rows"
    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return "Matrices have different number of columns"
    Result_Matrix=[]
    i=0
    while (i<len(A) and i<len(B)):
        j=0
        row=[]
        while(j<len(A[i])and j<len(B[i])):
            row.append(A[i][j]+B[i][j])
            j+=1
        Result_Matrix.append(row)
        i+=1
    return Result_Matrix
         
#Driver
# A=[[1,2,3],[4,5,6]]
# B=[[7,8,9],[2,3,5]]
# print(MatAdd(A,B))
#Task 03
def MatAddPartial(A, B, start, size):
    startingrow=start[0]
    startingcolumn=start[1]
    resultmatrix=[]
    i=startingrow
    while i<startingrow+size and i<len(A) and i<len(B):
        row=[]
        j=startingcolumn
        while j<startingcolumn+size and j<len(A[i]) and j<len(B[i]):
            row.append(A[i][j]+B[i][j])
            j+=1
        resultmatrix.append(row)
        i+=1
    return resultmatrix

#Driver
# A=[[1,2,3],[4,5,6]]
# B=[[7,8,9],[2,3,5]]
# print(MatAddPartial(A,B,(1,1),2))

#Task 04
def MatMul(A,B):
    if(len(A[0])!=len(B)):
        return "Matrices can not be multiplied."
    resultmatrix=[]
    for i in range(0,len(A),1):
        row=[]
        for j in range(0,len(B[0]),1):
            sum=0
            for k in range(0,len(A[0]),1):
                sum+=A[i][k]*B[k][j]
            row.append(sum)
        resultmatrix.append(row)
    return resultmatrix

# Driver
# A=[[1,2],[3,4]]
# B=[[5,7,9],[6,8,10]]
# print(MatMul(A,B))
# Task 05
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MatMulRecursive(A, B):
    # Base case: if the matrices are 1x1
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]

    n = len(A)  # Assuming A is square and n x n
    mid = n // 2

    # Split the matrices into quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Recursive multiplications
    C11 = add_matrices(MatMulRecursive(A11, B11), MatMulRecursive(A12, B21))
    C12 = add_matrices(MatMulRecursive(A11, B12), MatMulRecursive(A12, B22))
    C21 = add_matrices(MatMulRecursive(A21, B11), MatMulRecursive(A22, B21))
    C22 = add_matrices(MatMulRecursive(A21, B12), MatMulRecursive(A22, B22))

    # Combine results
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]

    return top + bottom

# Partition a matrix into 4 submatrices
def partition(M):
    n = len(M)
    m = len(M[0])
    mid_row = n // 2 + (n % 2)  # Adjust for odd number of rows
    mid_col = m // 2 + (m % 2)  # Adjust for odd number of columns

    # Padding the matrix with zeros if dimensions are odd
    A11 = [row[:mid_col] for row in M[:mid_row]]
    A12 = [row[mid_col:] + [0] * (mid_col - len(row[mid_col:])) for row in M[:mid_row]]
    A21 = [row[:mid_col] for row in M[mid_row:]] + [[0] * mid_col] * (mid_row - len(M[mid_row:]))
    A22 = [row[mid_col:] + [0] * (mid_col - len(row[mid_col:])) for row in M[mid_row:]] + [[0] * (m - mid_col)] * (mid_row - len(M[mid_row:]))
    
    return A11, A12, A21, A22

# Add two matrices
def MatAdd(A, B):
    n = len(A)
    m = len(A[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][j] + B[i][j]
    return result

# Combine four submatrices into one matrix
def combine(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom
# Driver code
# A=[[1,2],[3,4]]
# B=[[5,7,9],[6,8,10]]
# print(MatMulRecursive(A,B))

#Task 05
def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MatMulStrassen(A, B):
    n = len(A)
    
    # Base case: 1x1 matrix multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Splitting the matrices into quadrants
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate M1 to M7 using Strassen's formulas
    M1 = MatMulStrassen(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = MatMulStrassen(add_matrices(A21, A22), B11)
    M3 = MatMulStrassen(A11, subtract_matrices(B12, B22))
    M4 = MatMulStrassen(A22, subtract_matrices(B21, B11))
    M5 = MatMulStrassen(add_matrices(A11, A12), B22)
    M6 = MatMulStrassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = MatMulStrassen(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Calculate the final quadrants of the result matrix
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(add_matrices(subtract_matrices(M1, M2), M3), M6)

    # Combine the quadrants into a single result matrix
    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix

# Supporting functions
def MatAdd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MatSub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def pad_matrix(M, size):
    padded = [[0] * size for _ in range(size)]
    for i in range(len(M)):
        for j in range(len(M[0])):
            padded[i][j] = M[i][j]
    return padded

def partition(M):
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

def combine(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom
# Driver code
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# result = MatMulStrassen(A, B)
# print(result)
        





