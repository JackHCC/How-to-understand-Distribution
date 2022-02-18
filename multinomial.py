#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :multinomial.py
@Author  :JackHCC
@Date    :2022/2/18 13:24 
@Desc    :多项式分布【离散型】：与分类分布的关系与伯努尔分布与二项分布的关系相同，这里以三项分布为例

'''
import numpy as np
from matplotlib import pyplot as plt
from functools import reduce


def factorial(n: int) -> int:
    """
    get n!
    :param n:
    :return:
    """
    return reduce(int.__mul__, range(1, n + 1), 1)


def c(n: int, a: int, b: int, c: int) -> int:
    """
    C(n, a, b, v) = n! / a! * b! * c!, where a + b + c = n
    """
    assert a + b + c == n

    numerator = factorial(n)
    denominator = factorial(a) * factorial(b) * factorial(c)
    return numerator / denominator


def multinomial(n: int, p: list):
    """
    form：
    y = f(x_1, x_2, …… , x_k) =>
    specific form：
    y = C(n, x_1, ……, x_k) * p_1 ^ x_1 * …… * p_k ^ x_k , where x_1 + …… + x_k = n
    :param n:
    :param p:
    :return:
    """
    ls = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if i + j + k == n:
                    ls.append([i, j, k])

    assert len(p) == len(ls[0])

    y = [c(n, l[0], l[1], l[2]) * (p[0] ** l[0]) * (p[1] ** l[1]) * (p[2] ** l[2]) for l in ls]
    x = np.arange(len(y))
    return x, y


if __name__ == "__main__":
    p = [0.2, 0.3, 0.5]
    for n_experiment in [20, 21, 22]:
        x, y = multinomial(n_experiment, p)
        plt.scatter(x, y, label=r'$trial=%d$' % (n_experiment))

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("multinomial")
    plt.savefig('images/multinomial.png')
    plt.show()
