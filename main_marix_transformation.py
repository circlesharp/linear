## main_marix_transformation.py
## 第五章

import matplotlib.pyplot as plt
from Matrix import Matrix
from Vector import Vector
import math

if __name__ == "__main__":
    
    points = [[0,0], [0,5], [3,5], [3,4], [1,4],
              [1,3], [2,3], [2,2], [1,2], [1,0]]
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize = (5,5))  # figsize传入元组，单位英寸
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x,y)
    # plt.show()

    P = Matrix(points)

    # T = Matrix([[2, 0], [0, 1.5]])  # 拉伸
    # T = Matrix([[1, 0], [0, -1]])   # x轴翻转
    # T = Matrix([[-1, 0], [0, 1]])   # y轴翻转
    # T = Matrix([[-1, 0], [0, -1]])  # 原点翻转
    # T = Matrix([[1, 0.5], [0, 1]])  # x轴错切：斜体效果
    # T = Matrix([[1, 0], [0.5, 1]])  # y轴错切：书本翻页效果
    theta = math.pi/3  # 1/3Π（弧度制），60°
    # T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])  # 旋转 theta 角度
    T= Matrix([[0,-1],[1,0]])  # 矩阵就是空间，将图形放到新的空间（单位矩阵就是标准的空间）

    P2 = T.dot(P.T())
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()