## LinearSystemNorm.py
## 一般化的高斯-约旦消元法(version2)

from Matrix import Matrix
from Vector import Vector
from _global import is_zero

class LinearSystem:
    '''
    处理为方阵的线性系统。
    基于Vector为主
    '''
    def __init__(self, A, b):
        assert A.row_num() == len(b), 'row number of A must be equal to length of b'
        self._m = A.row_num()
        self._n = A.col_num()
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]  # self.Ab 是一个元素为Vector实例的列表
        self.pivots = []  # 区分主元列与自由列 / 还能计算出非零行数量

    def _max_row(self, index_i, index_j, n):
        '''
        找出有可能成为主元的行
        只对 index_i 负责
        '''
        best = self.Ab[index_i][index_j]    # 初始化best，假设i行j列为主元
        ret = index_i                     # 初始化ret，代表备选主元的行序号
        for i in range(index_i+1, n):
            if self.Ab[i][index_j] > best:  # 对于往后的i行index位的元素，如果比best大，就进行替换 best, ret
                best, ret = self.Ab[i][index_j], i  # best虽然不返回，但是记录了当前的最大值
        return ret  # 返回 ret 行，作为替换的行数

    def _forward(self):
        i, k = 0, 0
        while i<self._m and k<self._n:
            # 看Ab[i][k]位置是否可以是主元
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]  # 对换

            if is_zero(self.Ab[i][k]):  # 判断该主元是否为0。如果是，则往后推进一列，对k负责
                k += 1
            else:  # 当主元非0，主元归一，下列归0
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]  # 主元归一 （在定义Vector类的时候，已经定义了 __mul__, __rmul__, __turediv__ 等）
                for j in range(i+1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]  # 让主元下的元素变为0 ，因为i行的主元已经是1，所以直接与j行i列的元素相乘。
                self.pivots.append(k)  # k值就是主元列的列序号
                i += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n-1, -1, -1):  # 反向的高斯消元
            k = self.pivots[i]
            for j in range(i-1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]  # 反向的高斯消元
                
    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(' '.join(str(self.Ab[i][j]) for j in range(self._n)), end=' ')  # 用self._n不会打印出增广矩阵最后一列
            print('|', self.Ab[i][-1])

if __name__ == "__main__":
    # A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    # b = Vector([7, -11, 1])
    # ls = LinearSystem(A, b)
    # # print(ls.Ab)
    # ls.gauss_jordan_elimination()
    # ls.fancy_print()

    # A4 = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    # b4 = Vector([4, 32, 13])
    # ls4 = LinearSystem(A4, b4)
    # ls4.gauss_jordan_elimination()
    # ls4.fancy_print()

    A7 = Matrix([[1, -1, 2, 0, 3], 
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b7 = Vector([1, 5, 13 ,-1])
    ls7 = LinearSystem(A7, b7)
    ls7.gauss_jordan_elimination()
    ls7.fancy_print()

    A8 = Matrix([[2, 2], [2, 1], [1, 2]])
    b8 = Vector([3, 2.5, 7])
    ls8 = LinearSystem(A8, b8)
    ls8.gauss_jordan_elimination()
    ls8.fancy_print()

    An = Matrix([[1, 2, 0, 0],
                 [3, 4, 0, 0],
                 [0, 0, 1, 2],
                 [0, 0, 3, 4]])
    bn = Vector([1, 0, 0, 1])
    lsn = LinearSystem(An, bn)
    lsn.gauss_jordan_elimination()
    lsn.fancy_print()