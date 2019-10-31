import numpy as np

if __name__ == '__main__':
    
    # 矩阵的创建
    A = np.array([[1,2], [3,4]])
    print(A)

    # 矩阵的属性
    print(A.shape)
    print(A.T)

    # 获取矩阵的元素
    print('取矩阵的元素:', A[1, 1])
    print('取矩阵的行：%s, %s' % (A[0], A[0, :]))
    print('取矩阵的列：%s' % A[:, 0])

    # 矩阵的基本运算
    B = np.array([[5,6], [7,8]])
    print(A+B, A-B)
    print(10*A, A*10)
    print('（线性代数中无意义）element-wise mul:', A*B)
    print(A.dot(B))

    p = np.array([10, 100])
    print('广播——高维与低维运算', A+p, A+1)  # 一般不用广播，explicit is better than implicit
    print(A.dot(p))