## main_vector.py
## 第二章

from Vector import Vector

if __name__ == "__main__":

    vec = Vector([5,2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    k = 3
    print("{} * {} = {}".format(vec, k, vec * k))
    print("{} * {} = {}".format(k, vec, k * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)  # 基于类方法的调用，而非某个对象
    print(zero2)

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    print("normalize({}) = {}".format(vec, vec.normalize()))
    print("norm({}) = {}".format(vec.normalize(), vec.normalize().norm()))

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

    print(vec.dot(vec2))  # 向量点乘