## Vector.py
## 第二章

import math
from _global import EPSILON

class Vector:

    def __init__(self, lst):
        self._values = list(lst)  # 复制。如果只用引用，从外部修改有风险

    @classmethod  # O不依赖任何一个_values，所以是类方法
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)  # 列表乘法产生一个列表

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))  # self已经是可迭代的，详见__iter__

    def normalize(self):
        """返回向量的单位向量"""
        # return Vector([i/self.norm() for i in self])
        # return 1 / self.norm() * Vector(self._values)  # 避免重复计算向量的模；而且，当前只是实现乘法，没有除法。
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normlize error! norn is zero.")
        return Vector(self._values) / self.norm()

    def __add__(self, another):
        assert len(self) == len(another), "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])  # 返回新的对象，免得改变_values

    def __sub__(self, another):
        assert len(self) == len(another), "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def dot(self, another):
        """向量点乘，返回结果标量"""
        assert len(self) == len(another), "Error in dot product. Lenght of vectors must be same."
        return sum(a*b for a,b in zip(self,another))

    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""
        assert type(k) == int or type(k) == float, "Error in mul."  # 这个是我自己加的
        return Vector([a*k for a in self])

    def __rmul__(self, k):  # 反乘
        """返回数量乘法的结果向量：k * sefl"""
        return self * k  # 直接使用__mul__

    def __truediv__(self, k):  # 除法
        """返回数量除法的结果向量：self / k"""
        return 1 / k * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self
    
    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """
        返回向量的迭代器，
        因为不想直接使用_values（私有变量）
        """
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))