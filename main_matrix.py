## Martix.py
## 第四章

from Matrix import Matrix
from Vector import Vector

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    matrix2 = Matrix([[11,12], [13, 14], [15, 16]])
    print(matrix)
    print('matrix.shape = {}'.format(matrix.shape()))
    print('matrix.size = {}'.format(matrix.size()))
    print('len(matrix) = {}'.format(len(matrix)))
    print('matrix[0,1] = {}'.format(matrix[0, 1]))  # 0, 1 就是元组
    print('matrix_col_1 = {}'.format(matrix.col_vector(1)))
    print('matrix_row_1 = {}'.format(matrix.row_vector(1)))

    print('='*40, '\n', '\n矩阵基本运算\n矩阵加法\n', '='*30)
    print('matrix: \t%s' % matrix)
    print('matrix2: \t%s' % matrix2)
    print('matrix + matrix2 => %s' % (matrix + matrix2))
    print('matrix2 - matrix => %s' % (matrix2 - matrix))

    print('='*40, '\n', '\n矩阵基本运算\n矩阵数量乘法\n', '='*30)
    print('matrix: \t%s' % matrix)
    print(matrix * 2)
    print(2.5 * matrix)  # 右乘法
    print(matrix / 2)  # 除法
    print(+matrix, -matrix)

    print('='*40, '\n', '\n矩阵基本运算\n零矩阵\n', '='*30)
    print('zero_3_5 => %s' % Matrix.zero(3,5))

    print('='*40, '\n', '\n矩阵基本运算\n矩阵点乘\n', '='*30)
    vec = Vector([4, 5])
    matrix3 = Matrix([[1,2],[3,4]])
    matrix4 = Matrix([[5,6],[7,8]])
    print('matrix.dot(vec) = %s' % matrix.dot(vec))
    print('matrix3.dot(matrix4) = %s' % matrix3.dot(matrix4))
    print('matrix4.dot(matrix3) = %s' % matrix4.dot(matrix3))
    print('matrix.dot(Matrix.zero(2, 4)) = %s' % matrix.dot(Matrix.zero(2, 4)))
    print('Matrix.zero(4, 3).dot(matrix) = %s' % Matrix.zero(4, 3).dot(matrix))

    print('='*40, '\n', '\n矩阵基本运算\n矩阵转置\n', '='*30)
    print('matrix    => %s\nmatrix.T()=> %s' % (matrix, matrix.T()))