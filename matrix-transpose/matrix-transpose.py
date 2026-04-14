import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here

    n_rows = len(A)
    n_cols = len(A[0])

    result = np.full((n_cols,n_rows), 0, dtype=int)

    for i in range(n_rows):
        for j in range(n_cols):
            result[j][i] = A[i][j]

    return result
    pass
