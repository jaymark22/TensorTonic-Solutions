import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    '''
    Case 1: # of row <  # of column
        Case1_Original = [
            [2,-3,-2],
            [-6,8,-2]
            ]
        Case1_Transposed = [
            [2,-6] => Case1_Original[0][0], Case1_Original[1][0],
            [-3,8] => Case1_Original[0][1], Case1_Original[1][1],
            [-2,2] => Case1_Original[0][2], Case1_Original[1][2],
            ]

        Case2_orginal = [
            [7,2,-6],
            [-4,-8,9],
            [4,-2,-9]
        ]
        Case2_Transposed = [
           [7,-4,-4], => Case2_orgninal[0][0], Case2_orgina[1][0]
            [2,-8,-9],
            [-6,9,-9]
        
    '''
    rows = len(A)
    cols = len(A[0])
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = A[i][j]
    
    return np.array(transposed)

