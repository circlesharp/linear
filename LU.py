## LU.py
## 实现矩阵的LU分解

from Matrix import Matrix
from Vector import Vector
from _global import is_zero

def lu(matrix):
    assert matrix.row_num() == matrix.col_num(), 'matrix must be a square matrix'

    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        if is_zero(A[i][i]):
            return None, None  # 不能分解，返回L，U 都是空
        else:
            for j in range(i+1, n):
                p = A[j][i] / A[i][i]  # 倍数
                A[j] = A[j] - p * A[i]
                L[j][i] = p
    return Matrix(L), Matrix([A[i].underlying_list() for i in range(n)])

if __name__ == "__main__":
    A = Matrix([[1,2,4], [3,7,2], [2,3,3]])
    L, U = lu(A)
    print(L, U, sep='\n')