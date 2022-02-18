#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :How-to-understand-Distribution 
@File    :categorical.py
@Author  :JackHCC
@Date    :2022/2/18 13:02 
@Desc    :多伯努利称为分类分布【离散型】。交叉熵和采取负对数的多伯努利分布具有相同的形式。

'''
import numpy as np
import random
from matplotlib import pyplot as plt


def categorical(p: list, k: int) -> list:
    """
    form：
    y = f(k) =>
    specific form：
    y =  求积：(p_i ^ x_i) , p_i求和为1
    :param p:
    :param k:
    :return:
    """
    return p[k]


def statistic(p):
    """
    get expectation and variance by using statistical method
    :param p:
    :return:
    """
    u = np.sum(np.multiply(p, range(len(p))))
    s = np.sum(np.multiply((range(len(p)) - u) ** 2, p))
    return u, s


if __name__ == "__main__":
    n_experiment = 100
    p = [0.2, 0.1, 0.7]
    x = np.arange(n_experiment)
    y = []
    for _ in range(n_experiment):
        k = random.randint(0, len(p) - 1)
        pick = categorical(p, k)
        y.append(pick)

    u, s = statistic(p)
    plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("categorical")
    plt.legend()
    plt.savefig('images/categorical.png')
    plt.show()
