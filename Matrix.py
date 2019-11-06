## Martix.py
## 第四章
from Vector import Vector

class Matrix:
    
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]  # 对于二维列表每一列复制
    
    @classmethod
    def zero(cls, r, c):
        ''' 
        返回一个 r行 c列 的零矩阵
        类方法，不需要定义实例去创建零矩阵
        '''
        return cls([[0]*c for _ in range(r)])  # 区分 c, r 的含义： 内层列表的len就是col

    @classmethod
    def identity(cls, n):
        ''' 返回一个n行n列的单位矩阵 '''
        # iden = [[0 for i in range(n)] for j in range(n)]
        iden = [[0]*n for _ in range(n)]  # 老师的写法
        for i in range(n):
            iden[i][i] = 1
        return cls(iden)  # 我返回的是 Matrix(iden)

    def row_vector(self, index):
        ''' 返回矩阵第index个行向量 '''
        return Vector(self._values[index])
    def col_vector(self, index):
        ''' 返回矩阵第index个列向量 '''
        return Vector([row[index] for row in self._values])
    def __getitem__(self, pos):  # 是不是有点像花哨索引了~
        ''' 返回矩阵pos位置的元素（pos 是元组） '''
        r, c = pos
        return self._values[r][c]
    def underlying_list(self):
        ''' 返回向量的单位向量 '''
        return self._values[:]

    def size(self):
        ''' 返回矩阵的元素个数 '''
        r, c = self.shape()
        return r * c
    def row_num(self):
        return self.shape()[0]
    def col_num(self):
        return self.shape()[1]
    def shape(self):
        '''返回矩阵的形状：(行数, 列数) '''
        return len(self._values), len(self._values[0])
    __len__ = row_num  # 计算长度就是计算行数

    # 矩阵的基本运算
    def __add__(self, other):
        ''' 矩阵加法 add '''
        assert self.shape() == other.shape(), 'Error in add. Shape of matrixs must be same.'
        # 我的方法
        # return Matrix([[x+y for x,y in zip(i,j)] for i,j in zip(self._values, other._values)])
        # 老师的方法
        return Matrix([[a+b for a,b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])
        # 尝试向量加法......失败了
        # return Matrix([list(Vector(vecSelf) + Vector(vecOther) for vecSelf,vecOther in map(self._values, other._values))])

    def __sub__(self, other):
        ''' 矩阵减法 subtract '''
        assert self.shape() == other.shape(), 'Error in sub. Shape of matrixs must be same.'
        # return Matrix([[a-b for a,b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])
        return self + (other * -1)  # bravo~~ 通过数量乘法重载矩阵减法

    def __mul__(self, k):
        ''' 矩阵数量乘法 scalar-mul '''
        assert (isinstance(k, int) or isinstance(k, float)), 'Error in mul. k must be a number.'
        return Matrix([val * k for val in col] for col in self._values)
    __rmul__ = __mul__  # bravo~~

    def __truediv__(self, k):
        ''' 矩阵数量除法 self/k '''
        return self * (1/k)

    def __pos__(self):
        ''' 返回矩阵取正的结果 '''
        return self

    def __neg__(self):
        ''' 返回矩阵取负的结果 '''
        return self * -1

    def T(self):
        ''' 矩阵转置 '''
        # return Matrix([[row[_colNum] for row in self._values] for _colNum in range(self.col_num())])
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])  # 用列元素构造行

    def dot(self, another):
        '''
        返回矩阵乘法的结果
        矩阵点乘矩阵时候，调用了矩阵点乘向量
        矩阵点乘向量时候，调用了向量点乘向量
        我自己实现的，bravo~~
        '''
        if isinstance(another, Vector):
            assert self.col_num() == len(another), 'matrix.col_num()->%s must == vector.__len__()->%s' % (self.col_num(), len(another))
            # return Vector([Vector(vec).dot(another) for vec in self._values])
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        elif isinstance(another, Matrix):
            assert self.col_num() == another.row_num(), 'the col_num()->%s of the front matrix must == the row_num()->%s of the behind one' % (self.col_num(), another.row_num())
            # return Matrix([self.dot(Vector(vec)) for vec in another.T()._values]).T()
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())] for i in range(self.row_num())])
        else:
            return 'matrix\'s dot method must accept another matrix or a vector.'

    def __repr__(self):
        return "Matirx({})".format(self._values)
    __str__ = __repr__  # 其实这里可以省略

if __name__ == '__main__':
    matrix = Matrix([[1,2,3], [4,5,6]])
    matrix2 = Matrix([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    print(matrix.dot(matrix2))
    # print(matrix.dot(2))
    print(Matrix.identity(7))