## LinearSystem.py
## 高斯-约旦消元法(version1)

from Matrix import Matrix
from Vector import Vector

class LinearSystem:
    '''
    处理为方阵的线性系统。
    基于Vector为主
    '''
    def __init__(self, A, b):
        assert A.row_num() == len(b), 'row number of A must be equal to length of b'
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n  # todo: no this restriction
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]  # self.Ab 是一个元素为Vector实例的列表

    def _max_row(self, index, n):
        ''' 
        找到n行中，属于index行的主元最大的行
        返回 ret 
        '''
        best = self.Ab[index][index]    # 初始化best，代表index行的主元
        ret = index                     # 初始化ret，代表备选主元的行序号
        for i in range(index+1, n):
            if self.Ab[i][index] > best:  # 对于往后的i行index位的元素，如果比best大，就进行替换 best, ret
                best, ret = self.Ab[i][index], i  # best虽然不返回，但是记录了当前的最大值
        return ret  # 返回 ret 行，作为替换的行数

    def _forward(self):
        n = self._m  # n 为行数
        for i in range(n):
            # Ab[i][i]为主元
            max_row = self._max_row(i, n)  # 找到n行中，属于i行的主元最大的行序号
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]  # 对换
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]  # i 行让主元变成1 （在定义Vector类的时候，已经定义了 __mul__, __rmul__, __turediv__ 等）
            for j in range(i+1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]  # 让主元下的元素变为0 ，因为i行的主元已经是1，所以直接与j行i列的元素相乘。

    def _backward(self):
        n = self._m  # 行数
        for i in range(n-1, -1, -1):
            # Ab[i][i] 作为主元
            for j in range(i-1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]  # 反向的高斯消元
                
    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(' '.join(str(self.Ab[i][j]) for j in range(self._n)), end=' ')  # 用self._n不会打印出增广矩阵最后一列
            print('|', self.Ab[i][-1])

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    # print(ls.Ab)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    A4 = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    b4 = Vector([4, 32, 13])
    ls4 = LinearSystem(A4, b4)
    ls4.gauss_jordan_elimination()
    ls4.fancy_print()

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