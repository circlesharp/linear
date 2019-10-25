## main_numpy_vector.py
## 第三章

import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    vec = np.array([1, 2, 3])  # np的向量中，只能存储一种数据
    # vec[0] = 666  # np的向量是可以修改的
    # print(vec)

    # np.array的创建
    print(np.zeros(5))  # 默认浮点型
    print(np.ones(5))
    print(np.full(5, 666))  # 5个666（整型）

    # np.array的基本属性
    print(vec, type(vec))
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0], vec[-1], vec[:2])
    print(vec[0], vec[-1], type(vec[:2]))

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec+vec2))  # 向量加法
    print("{} - {} = {}".format(vec, vec2, vec-vec2))  # 向量减法
    print("{} * {} = {}".format(2, vec, 2 * vec))  # 数量乘法
    print("{} * {} = {}".format(vec, 2, vec * 2))  # 数量乘法
    print("{} * {} = {}".format(vec, vec2, vec * vec2))  # element-wise mult 没有数学意义的乘法 
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))  # 向量点乘
    
    # 规范化
    print(np.linalg.norm(vec))  # 向量的模
    print(vec / np.linalg.norm(vec))  # 向量的规范化 or 单位向量